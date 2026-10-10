import { test } from "node:test";
import assert from "node:assert/strict";
import { Pleaxy, PleaxyError } from "../src/index.ts";

function mockFetch(status: number, body: unknown, seen: Request[]) {
  return async (input: Request | string | URL, init?: RequestInit) => {
    const request = input instanceof Request ? input : new Request(input, init);
    seen.push(request);
    return new Response(body === undefined ? null : JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
  };
}

test("sends the API key to the workspace's URL", async () => {
  const seen: Request[] = [];
  const pleaxy = new Pleaxy({ apiKey: "key.secret", workspaceId: "reg_123.buyer", baseUrl: "https://api.example.test/", fetch: mockFetch(200, { id: "PO-1" }, seen) });
  const po = await pleaxy.purchaseOrders.getPurchaseOrder("PO-1", { buyer: "reg_9.buyer" });
  assert.equal(po.id, "PO-1");
  assert.equal(seen[0].url, "https://api.example.test/v1/workspaces/reg_123.buyer/purchase-orders/PO-1?buyer=reg_9.buyer");
  assert.equal(seen[0].method, "GET");
  assert.equal(seen[0].headers.get("x-api-key"), "key.secret");
});

test("sends a JSON body", async () => {
  const seen: Request[] = [];
  const pleaxy = new Pleaxy({ accessToken: "tok", workspaceId: "w", fetch: mockFetch(201, { id: "PO-2" }, seen) });
  await pleaxy.purchaseOrders.cancelPurchaseOrder("PO-2", { reason: "duplicate" });
  assert.equal(seen[0].url, "https://api.pleaxy.ai/v1/workspaces/w/purchase-orders/PO-2/cancel");
  assert.equal(seen[0].headers.get("authorization"), "Bearer tok");
  assert.deepEqual(await seen[0].json(), { reason: "duplicate" });
});

test("throws PleaxyError with the API's code", async () => {
  const pleaxy = new Pleaxy({ apiKey: "k", workspaceId: "w", fetch: mockFetch(409, { statusCode: 409, code: "PO_ID_AMBIGUOUS", message: "Two buyers issued PO-1" }, []) });
  await assert.rejects(pleaxy.purchaseOrders.getPurchaseOrder("PO-1"), (err: unknown) => {
    assert.ok(err instanceof PleaxyError);
    assert.equal(err.status, 409);
    assert.equal(err.code, "PO_ID_AMBIGUOUS");
    assert.match(err.message, /409 PO_ID_AMBIGUOUS: Two buyers issued PO-1/);
    return true;
  });
});

test("joins a validation error's messages", async () => {
  const pleaxy = new Pleaxy({ apiKey: "k", workspaceId: "w", fetch: mockFetch(400, { statusCode: 400, message: ["supplier should not be empty", "lineItems must be an array"], error: "Bad Request" }, []) });
  await assert.rejects(pleaxy.purchaseOrders.createPurchaseOrder({ supplier: "", lineItems: [] }), /400 supplier should not be empty; lineItems must be an array/);
});

test("requires a workspace and a credential", () => {
  assert.throws(() => new Pleaxy({ apiKey: "k", workspaceId: "" }), /workspaceId is required/);
  assert.throws(() => new Pleaxy({ workspaceId: "w" }), /apiKey or an accessToken/);
});
