// Package pleaxy is the official Go client for the Pleaxy API: purchase orders,
// invoices and settlement for cloud spend.
//
//	client, err := pleaxy.NewClient(pleaxy.Config{
//		APIKey:      os.Getenv("PLEAXY_API_KEY"),
//		WorkspaceID: os.Getenv("PLEAXY_WORKSPACE_ID"),
//	})
//	orders, err := client.ListPurchaseOrders(ctx, nil)
//
// Methods are named after the operations in the API Reference
// (CreatePurchaseOrder). A non-2xx response is returned as an *Error.
package pleaxy

//go:generate go run github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@v2.4.1 -config oapi-codegen.yaml ../openapi/pleaxy.json
//go:generate node scripts/generate-operations.mjs

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"net/url"
	"strings"
	"time"
)

// DefaultBaseURL is the API's origin.
const DefaultBaseURL = "https://api.pleaxy.ai"

// Config configures a Client.
type Config struct {
	// WorkspaceID is Company profile → Workspace ID in the Pleaxy console,
	// e.g. reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer. Every call is scoped to it.
	WorkspaceID string
	// APIKey is an API key, <keyId>.<secret>, minted by a workspace administrator. Sent as X-Api-Key.
	APIKey string
	// AccessToken is a signed-in session's access token, used instead of APIKey
	// for the few operations that need a person.
	AccessToken string
	// BaseURL is the API's origin. Default DefaultBaseURL; the client adds /v1/workspaces/<WorkspaceID>.
	BaseURL string
	// HTTPClient sends the requests. Default: an http.Client with a 30-second timeout.
	HTTPClient *http.Client
}

// Client calls the Pleaxy API for one workspace.
type Client struct {
	api *ClientWithResponses
}

// NewClient returns a Client for cfg.WorkspaceID.
func NewClient(cfg Config) (*Client, error) {
	if cfg.WorkspaceID == "" {
		return nil, errors.New("pleaxy: WorkspaceID is required (Company profile → Workspace ID in the Pleaxy console)")
	}
	if cfg.APIKey == "" && cfg.AccessToken == "" {
		return nil, errors.New("pleaxy: set APIKey or AccessToken")
	}
	base := cfg.BaseURL
	if base == "" {
		base = DefaultBaseURL
	}
	httpClient := cfg.HTTPClient
	if httpClient == nil {
		httpClient = &http.Client{Timeout: 30 * time.Second}
	}
	server := strings.TrimRight(base, "/") + "/v1/workspaces/" + url.PathEscape(cfg.WorkspaceID) + "/"
	api, err := NewClientWithResponses(server,
		WithHTTPClient(httpClient),
		WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
			if cfg.APIKey != "" {
				req.Header.Set("X-Api-Key", cfg.APIKey)
			} else {
				req.Header.Set("Authorization", "Bearer "+cfg.AccessToken)
			}
			return nil
		}),
	)
	if err != nil {
		return nil, err
	}
	return &Client{api: api}, nil
}

// Raw returns the underlying oapi-codegen client, for anything the methods
// don't cover (a response's headers, for one).
func (c *Client) Raw() *ClientWithResponses { return c.api }

// Error is returned for every non-2xx response.
type Error struct {
	// StatusCode is the HTTP status.
	StatusCode int
	// Code is the API's machine-readable reason when it names one, e.g. PO_ID_AMBIGUOUS.
	Code string
	// Message is what went wrong; validation failures are joined with "; ".
	Message string
	// Body is the raw response body.
	Body []byte
}

func (e *Error) Error() string {
	if e.Code != "" {
		return fmt.Sprintf("pleaxy: %d %s: %s", e.StatusCode, e.Code, e.Message)
	}
	return fmt.Sprintf("pleaxy: %d %s", e.StatusCode, e.Message)
}

func checkStatus(resp *http.Response, body []byte) error {
	if resp.StatusCode >= 200 && resp.StatusCode < 300 {
		return nil
	}
	e := &Error{StatusCode: resp.StatusCode, Body: body, Message: http.StatusText(resp.StatusCode)}
	var parsed struct {
		Code    string          `json:"code"`
		Message json.RawMessage `json:"message"`
	}
	if json.Unmarshal(body, &parsed) == nil {
		e.Code = parsed.Code
		var one string
		var many []string
		if json.Unmarshal(parsed.Message, &one) == nil && one != "" {
			e.Message = one
		} else if json.Unmarshal(parsed.Message, &many) == nil && len(many) > 0 {
			e.Message = strings.Join(many, "; ")
		}
	} else if len(body) > 0 {
		e.Message = string(body)
	}
	return e
}

// Ptr returns a pointer to v, for the optional fields of a request:
// Provider: pleaxy.Ptr(pleaxy.CreatePurchaseOrderInputProviderAws).
func Ptr[T any](v T) *T { return &v }
