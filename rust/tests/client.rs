use std::io::{BufRead, BufReader, Read, Write};
use std::net::TcpListener;
use std::thread;

use pleaxy::models::CancelPurchaseOrderInput;

/// The request a one-shot local server received.
struct Seen {
    request_line: String,
    headers: Vec<(String, String)>,
    body: String,
}

impl Seen {
    fn header(&self, name: &str) -> Option<&str> {
        self.headers
            .iter()
            .find(|(k, _)| k.eq_ignore_ascii_case(name))
            .map(|(_, v)| v.as_str())
    }
}

/// Serves one response, returns the base URL and a handle to the request it received.
fn serve(
    status: &'static str,
    content_type: &'static str,
    body: &'static str,
) -> (String, thread::JoinHandle<Seen>) {
    let listener = TcpListener::bind("127.0.0.1:0").unwrap();
    let url = format!("http://{}", listener.local_addr().unwrap());
    let handle = thread::spawn(move || {
        let (stream, _) = listener.accept().unwrap();
        let mut reader = BufReader::new(stream.try_clone().unwrap());
        let mut request_line = String::new();
        reader.read_line(&mut request_line).unwrap();
        let mut headers = Vec::new();
        loop {
            let mut line = String::new();
            reader.read_line(&mut line).unwrap();
            let line = line.trim_end();
            if line.is_empty() {
                break;
            }
            let (k, v) = line.split_once(':').unwrap();
            headers.push((k.trim().to_owned(), v.trim().to_owned()));
        }
        let length: usize = headers
            .iter()
            .find(|(k, _)| k.eq_ignore_ascii_case("content-length"))
            .map(|(_, v)| v.parse().unwrap())
            .unwrap_or(0);
        let mut buf = vec![0; length];
        reader.read_exact(&mut buf).unwrap();
        let mut stream = stream;
        write!(stream, "HTTP/1.1 {status}\r\nContent-Type: {content_type}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}", body.len()).unwrap();
        Seen {
            request_line: request_line.trim_end().to_owned(),
            headers,
            body: String::from_utf8(buf).unwrap(),
        }
    });
    (url, handle)
}

#[tokio::test]
async fn sends_the_api_key_to_the_workspace_url() {
    let (url, server) = serve(
        "200 OK",
        "application/json",
        r#"{"id":"PO-1","status":"draft","someNewField":1}"#,
    );
    let client = pleaxy::Client::builder()
        .base_url(format!("{url}/"))
        .api_key("key.secret")
        .workspace_id("reg_123.buyer")
        .build()
        .unwrap();
    let po = client
        .purchase_orders()
        .get_purchase_order("PO-1", Some("reg_9.buyer"))
        .await
        .unwrap();
    let seen = server.join().unwrap();
    assert_eq!(
        seen.request_line,
        "GET /v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer HTTP/1.1"
    );
    assert_eq!(seen.header("x-api-key"), Some("key.secret"));
    assert_eq!(seen.header("authorization"), None);
    assert_eq!(po.id, "PO-1");
}

#[tokio::test]
async fn sends_a_json_body_with_a_session_token() {
    let (url, server) = serve("201 Created", "application/json", r#"{"id":"PO-1"}"#);
    let client = pleaxy::Client::builder()
        .base_url(url)
        .access_token("tok")
        .workspace_id("w")
        .build()
        .unwrap();
    let mut input = CancelPurchaseOrderInput::new();
    input.reason = Some("duplicate".into());
    let po = client
        .purchase_orders()
        .cancel_purchase_order("PO-1", input)
        .await
        .unwrap();
    let seen = server.join().unwrap();
    assert_eq!(
        seen.request_line,
        "POST /v1/workspaces/w/purchase-orders/PO-1/cancel HTTP/1.1"
    );
    assert_eq!(seen.header("authorization"), Some("Bearer tok"));
    assert_eq!(seen.header("x-api-key"), None);
    assert_eq!(
        serde_json::from_str::<serde_json::Value>(&seen.body).unwrap(),
        serde_json::json!({ "reason": "duplicate" })
    );
    assert_eq!(po.id, "PO-1");
}

#[tokio::test]
async fn reads_the_api_error_code() {
    let (url, server) = serve(
        "409 Conflict",
        "application/json",
        r#"{"statusCode":409,"code":"PO_ID_AMBIGUOUS","message":"Two buyers issued PO-1"}"#,
    );
    let client = pleaxy::Client::builder()
        .base_url(url)
        .api_key("k")
        .workspace_id("w")
        .build()
        .unwrap();
    let err = client
        .purchase_orders()
        .get_purchase_order("PO-1", None)
        .await
        .unwrap_err();
    server.join().unwrap();
    let api = pleaxy::api_error(&err).unwrap();
    assert_eq!(
        (api.status, api.code.as_deref(), api.message.as_str()),
        (409, Some("PO_ID_AMBIGUOUS"), "Two buyers issued PO-1")
    );
}

#[tokio::test]
async fn joins_validation_messages() {
    let (url, server) = serve(
        "400 Bad Request",
        "application/json",
        r#"{"statusCode":400,"message":["a is wrong","b is wrong"],"error":"Bad Request"}"#,
    );
    let client = pleaxy::Client::builder()
        .base_url(url)
        .api_key("k")
        .workspace_id("w")
        .build()
        .unwrap();
    let err = client
        .purchase_orders()
        .list_purchase_orders(None, None)
        .await
        .unwrap_err();
    server.join().unwrap();
    assert_eq!(
        pleaxy::api_error(&err).unwrap().message,
        "a is wrong; b is wrong"
    );
}

#[tokio::test]
async fn returns_a_file_download_as_bytes() {
    let (url, server) = serve(
        "200 OK",
        "text/csv; charset=utf-8",
        "invoice,amount\nINV-1,10\n",
    );
    let client = pleaxy::Client::builder()
        .base_url(url)
        .api_key("k")
        .workspace_id("w")
        .build()
        .unwrap();
    let csv = client.invoices().get_payment_export("EXP-1").await.unwrap();
    let seen = server.join().unwrap();
    assert_eq!(
        seen.request_line,
        "GET /v1/workspaces/w/invoices/payment-exports/EXP-1 HTTP/1.1"
    );
    assert_eq!(seen.header("x-api-key"), Some("k"));
    assert_eq!(csv, b"invoice,amount\nINV-1,10\n");
}

#[test]
fn requires_a_workspace_and_a_credential() {
    assert!(matches!(
        pleaxy::Client::builder().api_key("k").build(),
        Err(pleaxy::BuildError::MissingWorkspaceId)
    ));
    assert!(matches!(
        pleaxy::Client::builder().workspace_id("w").build(),
        Err(pleaxy::BuildError::MissingCredential)
    ));
}
