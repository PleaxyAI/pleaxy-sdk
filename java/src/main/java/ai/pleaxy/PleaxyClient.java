package ai.pleaxy;

import ai.pleaxy.api.ApiKeysApi;
import ai.pleaxy.api.ApprovalSettingsApi;
import ai.pleaxy.api.ApprovalsApi;
import ai.pleaxy.api.AutomationRulesApi;
import ai.pleaxy.api.BillingApi;
import ai.pleaxy.api.CloudConnectionsApi;
import ai.pleaxy.api.EmployeesApi;
import ai.pleaxy.api.ExchangeRatesApi;
import ai.pleaxy.api.InvoicesApi;
import ai.pleaxy.api.NotificationsApi;
import ai.pleaxy.api.OrgProfilesApi;
import ai.pleaxy.api.PurchaseOrdersApi;
import ai.pleaxy.api.SettlementApi;
import ai.pleaxy.api.SupplierConnectionsApi;
import ai.pleaxy.api.WorkspacesApi;
import ai.pleaxy.client.ApiClient;
import ai.pleaxy.client.ApiException;
import ai.pleaxy.model.ApiError;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.Objects;
import java.util.Optional;

/**
 * The Pleaxy API client, scoped to one workspace.
 *
 * <pre>{@code
 * PleaxyClient client = PleaxyClient.builder()
 *     .apiKey(System.getenv("PLEAXY_API_KEY"))
 *     .workspaceId(System.getenv("PLEAXY_WORKSPACE_ID"))
 *     .build();
 * List<ListPurchaseOrdersItem> orders = client.purchaseOrders().listPurchaseOrders(null, null);
 * }</pre>
 *
 * <p>Operations are grouped by API area ({@link #purchaseOrders()}, {@link #invoices()}, ...) and named after
 * the operations in the API Reference (CreatePurchaseOrder is {@code purchaseOrders().createPurchaseOrder}). A
 * non-2xx response throws {@link ApiException}; {@link #error(ApiException)} reads the API's error body.
 */
public final class PleaxyClient {
  /** The API's origin. */
  public static final String DEFAULT_BASE_URL = "https://api.pleaxy.ai";

  private final ApiClient apiClient;
  private final ApiKeysApi apiKeys;
  private final ApprovalSettingsApi approvalSettings;
  private final ApprovalsApi approvals;
  private final AutomationRulesApi automationRules;
  private final BillingApi billing;
  private final CloudConnectionsApi cloudConnections;
  private final EmployeesApi employees;
  private final ExchangeRatesApi exchangeRates;
  private final InvoicesApi invoices;
  private final NotificationsApi notifications;
  private final OrgProfilesApi orgProfiles;
  private final PurchaseOrdersApi purchaseOrders;
  private final SettlementApi settlement;
  private final SupplierConnectionsApi supplierConnections;
  private final WorkspacesApi workspaces;

  private PleaxyClient(Builder builder) {
    if (builder.workspaceId == null || builder.workspaceId.isEmpty()) {
      throw new IllegalArgumentException("Pleaxy: workspaceId is required (Company profile → Workspace ID in the Pleaxy console).");
    }
    if (isBlank(builder.apiKey) && isBlank(builder.accessToken)) {
      throw new IllegalArgumentException("Pleaxy: set an apiKey or an accessToken.");
    }
    String origin = builder.baseUrl.replaceAll("/+$", "");
    String workspace = URLEncoder.encode(builder.workspaceId, StandardCharsets.UTF_8).replace("+", "%20");
    ApiClient apiClient = new ApiClient();
    apiClient.updateBaseUri(origin + "/v1/workspaces/" + workspace);
    apiClient.setReadTimeout(builder.timeout);
    if (builder.httpClientBuilder != null) {
      apiClient.setHttpClientBuilder(builder.httpClientBuilder);
    }
    String apiKey = builder.apiKey;
    String accessToken = builder.accessToken;
    apiClient.setRequestInterceptor(request -> {
      if (!isBlank(apiKey)) {
        request.header("X-Api-Key", apiKey);
      } else {
        request.header("Authorization", "Bearer " + accessToken);
      }
    });
    this.apiClient = apiClient;
    this.apiKeys = new ApiKeysApi(apiClient);
    this.approvalSettings = new ApprovalSettingsApi(apiClient);
    this.approvals = new ApprovalsApi(apiClient);
    this.automationRules = new AutomationRulesApi(apiClient);
    this.billing = new BillingApi(apiClient);
    this.cloudConnections = new CloudConnectionsApi(apiClient);
    this.employees = new EmployeesApi(apiClient);
    this.exchangeRates = new ExchangeRatesApi(apiClient);
    this.invoices = new InvoicesApi(apiClient);
    this.notifications = new NotificationsApi(apiClient);
    this.orgProfiles = new OrgProfilesApi(apiClient);
    this.purchaseOrders = new PurchaseOrdersApi(apiClient);
    this.settlement = new SettlementApi(apiClient);
    this.supplierConnections = new SupplierConnectionsApi(apiClient);
    this.workspaces = new WorkspacesApi(apiClient);
  }

  public static Builder builder() {
    return new Builder();
  }

  /** The underlying generated client, for anything the API classes don't cover. */
  public ApiClient apiClient() {
    return apiClient;
  }

  /** ApiKeys operations. */
  public ApiKeysApi apiKeys() {
    return apiKeys;
  }

  /** ApprovalSettings operations. */
  public ApprovalSettingsApi approvalSettings() {
    return approvalSettings;
  }

  /** Approvals operations. */
  public ApprovalsApi approvals() {
    return approvals;
  }

  /** AutomationRules operations. */
  public AutomationRulesApi automationRules() {
    return automationRules;
  }

  /** Billing operations. */
  public BillingApi billing() {
    return billing;
  }

  /** CloudConnections operations. */
  public CloudConnectionsApi cloudConnections() {
    return cloudConnections;
  }

  /** Employees operations. */
  public EmployeesApi employees() {
    return employees;
  }

  /** ExchangeRates operations. */
  public ExchangeRatesApi exchangeRates() {
    return exchangeRates;
  }

  /** Invoices operations. */
  public InvoicesApi invoices() {
    return invoices;
  }

  /** Notifications operations. */
  public NotificationsApi notifications() {
    return notifications;
  }

  /** OrgProfiles operations. */
  public OrgProfilesApi orgProfiles() {
    return orgProfiles;
  }

  /** PurchaseOrders operations. */
  public PurchaseOrdersApi purchaseOrders() {
    return purchaseOrders;
  }

  /** Settlement operations. */
  public SettlementApi settlement() {
    return settlement;
  }

  /** SupplierConnections operations. */
  public SupplierConnectionsApi supplierConnections() {
    return supplierConnections;
  }

  /** Workspaces operations. */
  public WorkspacesApi workspaces() {
    return workspaces;
  }

  /**
   * The API's error body - {@code statusCode}, the machine-readable {@code code} when it names one (e.g.
   * {@code PO_ID_AMBIGUOUS}) and {@code message} - or empty when the response had none.
   */
  public Optional<ApiError> error(ApiException e) {
    if (isBlank(e.getResponseBody())) {
      return Optional.empty();
    }
    try {
      return Optional.of(apiClient.getObjectMapper().readValue(e.getResponseBody(), ApiError.class));
    } catch (Exception parseError) {
      return Optional.empty();
    }
  }

  private static boolean isBlank(String value) {
    return value == null || value.isEmpty();
  }

  /** Builds a {@link PleaxyClient}. */
  public static final class Builder {
    private String baseUrl = DEFAULT_BASE_URL;
    private String workspaceId;
    private String apiKey;
    private String accessToken;
    private Duration timeout = Duration.ofSeconds(30);
    private HttpClient.Builder httpClientBuilder;

    private Builder() {}

    /** The API's origin. Default {@value PleaxyClient#DEFAULT_BASE_URL}; the client adds /v1/workspaces/&lt;workspaceId&gt;. */
    public Builder baseUrl(String baseUrl) {
      this.baseUrl = Objects.requireNonNull(baseUrl);
      return this;
    }

    /** Company profile → Workspace ID in the Pleaxy console, e.g. reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer. */
    public Builder workspaceId(String workspaceId) {
      this.workspaceId = workspaceId;
      return this;
    }

    /** An API key, &lt;keyId&gt;.&lt;secret&gt;, minted by a workspace administrator. Sent as X-Api-Key. */
    public Builder apiKey(String apiKey) {
      this.apiKey = apiKey;
      return this;
    }

    /** A signed-in session's access token, instead of an API key, for the few operations that need a person. */
    public Builder accessToken(String accessToken) {
      this.accessToken = accessToken;
      return this;
    }

    /** How long to wait for a response. Default 30 seconds. */
    public Builder timeout(Duration timeout) {
      this.timeout = Objects.requireNonNull(timeout);
      return this;
    }

    /** The {@link HttpClient.Builder} the requests are sent with, e.g. for a proxy. */
    public Builder httpClientBuilder(HttpClient.Builder httpClientBuilder) {
      this.httpClientBuilder = httpClientBuilder;
      return this;
    }

    public PleaxyClient build() {
      return new PleaxyClient(this);
    }
  }
}
