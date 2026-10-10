import { Resources } from "./operations.js";
import { Transport } from "./transport.js";

export interface PleaxyOptions {
  /**
   * Your workspace's ID: Company profile → Workspace ID in the Pleaxy console,
   * e.g. `reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer`. Every call is scoped to it.
   */
  workspaceId: string;
  /** An API key, `<keyId>.<secret>`, minted by a workspace administrator. Sent as `X-Api-Key`. */
  apiKey?: string;
  /** A signed-in session's access token instead of an API key, for the few operations that need a person. */
  accessToken?: string;
  /** The API's origin. Default `https://api.pleaxy.ai`; the SDK adds `/v1/workspaces/<workspaceId>`. */
  baseUrl?: string;
  /** Headers sent with every call. */
  headers?: Record<string, string>;
  /** A fetch implementation, for runtimes without a global one or for testing. */
  fetch?: typeof globalThis.fetch;
}

export const DEFAULT_BASE_URL = "https://api.pleaxy.ai";

/**
 * The Pleaxy API client.
 *
 * ```ts
 * const pleaxy = new Pleaxy({ apiKey: process.env.PLEAXY_API_KEY, workspaceId: process.env.PLEAXY_WORKSPACE_ID! });
 * const orders = await pleaxy.purchaseOrders.listPurchaseOrders();
 * ```
 *
 * Methods are grouped by API area and named after the operations in the API
 * Reference (CreatePurchaseOrder -> `purchaseOrders.createPurchaseOrder`).
 * A failed call throws a {@link PleaxyError}.
 */
export class Pleaxy extends Resources {
  /** The underlying openapi-fetch client, typed against the whole API. */
  readonly raw: Transport["raw"];

  constructor(options: PleaxyOptions) {
    if (!options?.workspaceId) throw new Error("Pleaxy: workspaceId is required (Company profile → Workspace ID in the Pleaxy console).");
    if (!options.apiKey && !options.accessToken) throw new Error("Pleaxy: pass an apiKey or an accessToken.");
    const headers: Record<string, string> = { ...options.headers };
    if (options.apiKey) headers["X-Api-Key"] = options.apiKey;
    else headers.Authorization = `Bearer ${options.accessToken}`;
    const transport = new Transport({ baseUrl: options.baseUrl ?? DEFAULT_BASE_URL, workspaceId: options.workspaceId, headers, fetch: options.fetch });
    super(transport);
    this.raw = transport.raw;
  }
}

export { PleaxyError } from "./transport.js";
export type { RequestOptions, RequestBody, QueryParams, ResponseBody, ApiErrorBody } from "./transport.js";
export type { components, operations, paths } from "./schema.js";
export * from "./operations.js";

import type { components } from "./schema.js";
type Schemas = components["schemas"];
export type PurchaseOrder = Schemas["PurchaseOrder"];
export type PurchaseOrderSupplierView = Schemas["PurchaseOrderSupplierView"];
export type InvoiceBuyerView = Schemas["InvoiceBuyerView"];
export type InvoiceSupplierView = Schemas["InvoiceSupplierView"];
export type CreatePurchaseOrderInput = Schemas["CreatePurchaseOrderInput"];
export type LineItemInput = Schemas["LineItemInput"];
