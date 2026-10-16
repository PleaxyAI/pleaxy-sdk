use std::fmt;
use std::time::Duration;

use crate::apis::configuration::{ApiKey, Configuration};
use crate::apis::Error;

/// The API's origin.
pub const DEFAULT_BASE_URL: &str = "https://api.pleaxy.ai";

/// The Pleaxy API client, scoped to one workspace. Cheap to clone.
#[derive(Debug, Clone)]
pub struct Client {
    pub(crate) config: Configuration,
}

impl Client {
    pub fn builder() -> ClientBuilder {
        ClientBuilder::default()
    }

    /// The generated configuration, to call a function in [`crate::apis`] directly.
    pub fn configuration(&self) -> &Configuration {
        &self.config
    }
}

/// Builds a [`Client`].
#[derive(Debug, Default)]
pub struct ClientBuilder {
    base_url: Option<String>,
    workspace_id: Option<String>,
    api_key: Option<String>,
    access_token: Option<String>,
    timeout: Option<Duration>,
    http_client: Option<reqwest::Client>,
}

impl ClientBuilder {
    /// The API's origin. Default [`DEFAULT_BASE_URL`]; the client adds `/v1/workspaces/<workspace_id>`.
    pub fn base_url(mut self, base_url: impl Into<String>) -> Self {
        self.base_url = Some(base_url.into());
        self
    }

    /// Company profile → Workspace ID in the Pleaxy console, e.g. `reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer`.
    pub fn workspace_id(mut self, workspace_id: impl Into<String>) -> Self {
        self.workspace_id = Some(workspace_id.into());
        self
    }

    /// An API key, `<keyId>.<secret>`, minted by a workspace administrator. Sent as `X-Api-Key`.
    pub fn api_key(mut self, api_key: impl Into<String>) -> Self {
        self.api_key = Some(api_key.into());
        self
    }

    /// A signed-in session's access token instead of an API key, for the few operations that need a person.
    pub fn access_token(mut self, access_token: impl Into<String>) -> Self {
        self.access_token = Some(access_token.into());
        self
    }

    /// How long to wait for a response. Default 30 seconds. Ignored with [`ClientBuilder::http_client`].
    pub fn timeout(mut self, timeout: Duration) -> Self {
        self.timeout = Some(timeout);
        self
    }

    /// The `reqwest::Client` requests are sent with, e.g. for a proxy.
    pub fn http_client(mut self, http_client: reqwest::Client) -> Self {
        self.http_client = Some(http_client);
        self
    }

    pub fn build(self) -> Result<Client, BuildError> {
        let workspace_id = self
            .workspace_id
            .filter(|w| !w.is_empty())
            .ok_or(BuildError::MissingWorkspaceId)?;
        let api_key = self.api_key.filter(|k| !k.is_empty());
        let access_token = self.access_token.filter(|t| !t.is_empty());
        if api_key.is_none() && access_token.is_none() {
            return Err(BuildError::MissingCredential);
        }
        let origin = self
            .base_url
            .as_deref()
            .unwrap_or(DEFAULT_BASE_URL)
            .trim_end_matches('/');
        let mut base =
            url::Url::parse(origin).map_err(|_| BuildError::InvalidBaseUrl(origin.to_owned()))?;
        base.path_segments_mut()
            .map_err(|_| BuildError::InvalidBaseUrl(origin.to_owned()))?
            .pop_if_empty()
            .extend(["v1", "workspaces", workspace_id.as_str()]);

        let http_client = match self.http_client {
            Some(client) => client,
            None => reqwest::Client::builder()
                .timeout(self.timeout.unwrap_or(Duration::from_secs(30)))
                .build()
                .map_err(BuildError::Http)?,
        };
        let config = Configuration {
            base_path: base.as_str().trim_end_matches('/').to_owned(),
            user_agent: Some(concat!("pleaxy-rust/", env!("CARGO_PKG_VERSION")).to_owned()),
            client: http_client,
            basic_auth: None,
            oauth_access_token: None,
            // One credential only: the generated functions send every one that is set.
            api_key: api_key.as_ref().map(|key| ApiKey {
                prefix: None,
                key: key.clone(),
            }),
            bearer_access_token: if api_key.is_some() {
                None
            } else {
                access_token
            },
        };
        Ok(Client { config })
    }
}

/// Why [`ClientBuilder::build`] failed.
#[derive(Debug)]
pub enum BuildError {
    MissingWorkspaceId,
    MissingCredential,
    InvalidBaseUrl(String),
    Http(reqwest::Error),
}

impl fmt::Display for BuildError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            BuildError::MissingWorkspaceId => write!(f, "pleaxy: workspace_id is required (Company profile → Workspace ID in the Pleaxy console)"),
            BuildError::MissingCredential => write!(f, "pleaxy: set an api_key or an access_token"),
            BuildError::InvalidBaseUrl(url) => write!(f, "pleaxy: invalid base_url {url}"),
            BuildError::Http(err) => write!(f, "pleaxy: {err}"),
        }
    }
}

impl std::error::Error for BuildError {}

/// The API's error body: the HTTP status, the machine-readable `code` when the API names one
/// (e.g. `PO_ID_AMBIGUOUS`) and the `message` (validation messages joined with "; ").
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ApiErrorBody {
    pub status: u16,
    pub code: Option<String>,
    pub message: String,
}

/// The API's error body for a non-2xx response, or `None` for any other error (network,
/// a body that isn't JSON).
pub fn api_error<T>(err: &Error<T>) -> Option<ApiErrorBody> {
    let Error::ResponseError(response) = err else {
        return None;
    };
    let body: serde_json::Value = serde_json::from_str(&response.content).ok()?;
    let message = match body.get("message") {
        Some(serde_json::Value::String(one)) => one.clone(),
        Some(serde_json::Value::Array(many)) => many
            .iter()
            .filter_map(|m| m.as_str())
            .collect::<Vec<_>>()
            .join("; "),
        _ => response
            .status
            .canonical_reason()
            .unwrap_or_default()
            .to_owned(),
    };
    Some(ApiErrorBody {
        status: response.status.as_u16(),
        code: body.get("code").and_then(|c| c.as_str()).map(str::to_owned),
        message,
    })
}

impl Client {
    /// GETs or POSTs a file download (a payment export's CSV, a remittance advice PDF) and returns its bytes.
    /// The generated functions for these parse the body as JSON, so src/resources.rs calls this instead.
    pub(crate) async fn download<T: serde::de::DeserializeOwned, B: serde::Serialize>(
        &self,
        method: reqwest::Method,
        path: &str,
        query: &[(&str, Option<&str>)],
        body: Option<&B>,
    ) -> Result<Vec<u8>, Error<T>> {
        let config = &self.config;
        let mut request = config
            .client
            .request(method, format!("{}{}", config.base_path, path));
        if let Some(body) = body {
            request = request.json(body);
        }
        let query: Vec<(&str, &str)> = query
            .iter()
            .filter_map(|(k, v)| v.map(|v| (*k, v)))
            .collect();
        if !query.is_empty() {
            request = request.query(&query);
        }
        if let Some(agent) = &config.user_agent {
            request = request.header(reqwest::header::USER_AGENT, agent);
        }
        if let Some(key) = &config.api_key {
            request = request.header("X-Api-Key", &key.key);
        } else if let Some(token) = &config.bearer_access_token {
            request = request.bearer_auth(token);
        }
        let response = request.send().await?;
        let status = response.status();
        if status.is_success() {
            return Ok(response.bytes().await?.to_vec());
        }
        let content = response.text().await?;
        let entity = serde_json::from_str(&content).ok();
        Err(Error::ResponseError(crate::apis::ResponseContent {
            status,
            content,
            entity,
        }))
    }
}
