// The quickstart on pleaxy.ai/sdks. Built in CI (go vet ./...), so it can't drift from the SDK.
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/pleaxyai/pleaxy-sdk/go"
)

func main() {
	client, err := pleaxy.NewClient(pleaxy.Config{
		APIKey:      os.Getenv("PLEAXY_API_KEY"),
		WorkspaceID: os.Getenv("PLEAXY_WORKSPACE_ID"),
	})
	if err != nil {
		log.Fatal(err)
	}

	po, err := client.CreatePurchaseOrder(context.Background(), pleaxy.CreatePurchaseOrderInput{
		Supplier: "Amazon Web Services",
		Provider: pleaxy.Ptr(pleaxy.CreatePurchaseOrderInputProviderAws),
		LineItems: []pleaxy.LineItemInput{
			{
				ScopeType:    pleaxy.LineItemInputScopeTypeSku,
				ScopeId:      pleaxy.Ptr("AWS-EC2-M5LG"),
				Name:         "EC2 m5.large",
				RuleType:     pleaxy.LineItemInputRuleTypeQuantity,
				Unit:         "hr",
				UnitPrice:    0.096,
				Qty:          5000,
				NteAmount:    0,
				PaymentTerms: "Net 30",
				ValidFrom:    "2026-01-01",
				ValidUntil:   "2026-12-31",
			},
		},
	})
	var apiErr *pleaxy.Error
	if errors.As(err, &apiErr) {
		log.Fatalf("%d %s: %s", apiErr.StatusCode, apiErr.Code, apiErr.Message)
	} else if err != nil {
		log.Fatal(err)
	}
	fmt.Println(po.Id, *po.Status)
}
