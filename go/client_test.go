package pleaxy_test

import (
	"context"
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/pleaxyai/pleaxy-sdk/go"
)

func server(t *testing.T, status int, body string, seen *[]*http.Request, bodies *[]string) *httptest.Server {
	return serverOf(t, "application/json", status, body, seen, bodies)
}

func serverOf(t *testing.T, contentType string, status int, body string, seen *[]*http.Request, bodies *[]string) *httptest.Server {
	t.Helper()
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		b, _ := io.ReadAll(r.Body)
		*seen = append(*seen, r)
		*bodies = append(*bodies, string(b))
		w.Header().Set("Content-Type", contentType)
		w.WriteHeader(status)
		_, _ = io.WriteString(w, body)
	}))
	t.Cleanup(srv.Close)
	return srv
}

func TestSendsTheAPIKeyToTheWorkspaceURL(t *testing.T) {
	var seen []*http.Request
	var bodies []string
	srv := server(t, 200, `{"id":"PO-1","status":"draft"}`, &seen, &bodies)
	client, err := pleaxy.NewClient(pleaxy.Config{APIKey: "key.secret", WorkspaceID: "reg_123.buyer", BaseURL: srv.URL + "/"})
	if err != nil {
		t.Fatal(err)
	}
	result, err := client.GetPurchaseOrder(context.Background(), "PO-1", &pleaxy.GetPurchaseOrderParams{Buyer: pleaxy.Ptr("reg_9.buyer")})
	if err != nil {
		t.Fatal(err)
	}
	if got := seen[0].URL.String(); got != "/v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer" {
		t.Errorf("URL = %s", got)
	}
	if got := seen[0].Header.Get("X-Api-Key"); got != "key.secret" {
		t.Errorf("X-Api-Key = %q", got)
	}
	po, err := result.AsPurchaseOrder()
	if err != nil || po.Id != "PO-1" {
		t.Errorf("po = %+v, %v", po, err)
	}
}

func TestSendsAJSONBodyWithASessionToken(t *testing.T) {
	var seen []*http.Request
	var bodies []string
	srv := server(t, 201, `{"id":"PO-1"}`, &seen, &bodies)
	client, _ := pleaxy.NewClient(pleaxy.Config{AccessToken: "tok", WorkspaceID: "w", BaseURL: srv.URL})
	po, err := client.CancelPurchaseOrder(context.Background(), "PO-1", pleaxy.CancelPurchaseOrderInput{Reason: pleaxy.Ptr("duplicate")})
	if err != nil {
		t.Fatal(err)
	}
	if seen[0].Method != "POST" || seen[0].URL.Path != "/v1/workspaces/w/purchase-orders/PO-1/cancel" {
		t.Errorf("%s %s", seen[0].Method, seen[0].URL.Path)
	}
	if got := seen[0].Header.Get("Authorization"); got != "Bearer tok" {
		t.Errorf("Authorization = %q", got)
	}
	var body map[string]any
	_ = json.Unmarshal([]byte(bodies[0]), &body)
	if body["reason"] != "duplicate" {
		t.Errorf("body = %s", bodies[0])
	}
	if po.Id != "PO-1" {
		t.Errorf("po.Id = %s", po.Id)
	}
}

func TestReturnsAnErrorWithTheAPICode(t *testing.T) {
	var seen []*http.Request
	var bodies []string
	srv := server(t, 409, `{"statusCode":409,"code":"PO_ID_AMBIGUOUS","message":"Two buyers issued PO-1"}`, &seen, &bodies)
	client, _ := pleaxy.NewClient(pleaxy.Config{APIKey: "k", WorkspaceID: "w", BaseURL: srv.URL})
	_, err := client.GetPurchaseOrder(context.Background(), "PO-1", nil)
	var apiErr *pleaxy.Error
	if !errors.As(err, &apiErr) {
		t.Fatalf("err = %v", err)
	}
	if apiErr.StatusCode != 409 || apiErr.Code != "PO_ID_AMBIGUOUS" || err.Error() != "pleaxy: 409 PO_ID_AMBIGUOUS: Two buyers issued PO-1" {
		t.Errorf("err = %v", err)
	}
}

func TestJoinsValidationMessages(t *testing.T) {
	var seen []*http.Request
	var bodies []string
	srv := server(t, 400, `{"statusCode":400,"message":["a is wrong","b is wrong"],"error":"Bad Request"}`, &seen, &bodies)
	client, _ := pleaxy.NewClient(pleaxy.Config{APIKey: "k", WorkspaceID: "w", BaseURL: srv.URL})
	_, err := client.ListPurchaseOrders(context.Background(), nil)
	if err == nil || err.Error() != "pleaxy: 400 a is wrong; b is wrong" {
		t.Errorf("err = %v", err)
	}
}

func TestReturnsAFileDownloadAsBytes(t *testing.T) {
	var seen []*http.Request
	var bodies []string
	srv := serverOf(t, "text/csv; charset=utf-8", 200, "invoice,amount\nINV-1,10\n", &seen, &bodies)
	client, _ := pleaxy.NewClient(pleaxy.Config{APIKey: "k", WorkspaceID: "w", BaseURL: srv.URL})
	csv, err := client.GetPaymentExport(context.Background(), "EXP-1")
	if err != nil || string(csv) != "invoice,amount\nINV-1,10\n" {
		t.Errorf("csv = %q, %v", csv, err)
	}
}

func TestRequiresAWorkspaceAndACredential(t *testing.T) {
	if _, err := pleaxy.NewClient(pleaxy.Config{APIKey: "k"}); err == nil {
		t.Error("no error without WorkspaceID")
	}
	if _, err := pleaxy.NewClient(pleaxy.Config{WorkspaceID: "w"}); err == nil {
		t.Error("no error without a credential")
	}
}
