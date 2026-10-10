import createClient, { type Client } from "openapi-fetch";
import type { components, operations, paths } from "./schema.js";

type Operation<K extends keyof operations> = operations[K];
type JsonOf<T> = T extends { content: { "application/json": infer B } } ? B : never;
type JsonOrVoid<T> = T extends { content: { "application/json": infer B } } ? B : void;
type SuccessCode = 200 | 201 | 202 | 204;

/** The JSON body an operation takes. */
export type RequestBody<K extends keyof operations> = JsonOf<NonNullable<Operation<K>["requestBody"]>>;
/** An operation's query parameters. */
export type QueryParams<K extends keyof operations> = NonNullable<Operation<K>["parameters"]["query"]>;
/** The JSON body an operation returns on success. */
export type ResponseBody<K extends keyof operations> = JsonOrVoid<Operation<K>["responses"][Extract<keyof Operation<K>["responses"], SuccessCode>]>;

export type ApiErrorBody = components["schemas"]["ApiError"];

export interface RequestOptions {
  /** Extra headers for this call only. */
  headers?: Record<string, string>;
  /** Abort the call, e.g. with `AbortSignal.timeout(10_000)`. */
  signal?: AbortSignal;
}

/** Thrown for every non-2xx response. `code` is the API's machine-readable reason when it names one (e.g. "PO_ID_AMBIGUOUS"). */
export class PleaxyError extends Error {
  readonly status: number;
  readonly code: string | undefined;
  readonly body: ApiErrorBody | unknown;
  readonly response: Response;

  constructor(response: Response, body: unknown) {
    const error = (typeof body === "object" && body !== null ? body : {}) as Partial<ApiErrorBody>;
    const message = Array.isArray(error.message) ? error.message.join("; ") : (error.message ?? (typeof body === "string" && body ? body : response.statusText));
    super(`${response.status} ${error.code ? `${error.code}: ` : ""}${message}`);
    this.name = "PleaxyError";
    this.status = response.status;
    this.code = error.code;
    this.body = body;
    this.response = response;
  }
}

export interface TransportConfig {
  baseUrl: string;
  workspaceId: string;
  headers: Record<string, string>;
  fetch?: typeof globalThis.fetch;
}

export class Transport {
  /** The underlying openapi-fetch client, for anything the methods don't cover (response headers, for one). */
  readonly raw: Client<paths>;

  constructor(config: TransportConfig) {
    const origin = config.baseUrl.replace(/\/+$/, "");
    this.raw = createClient<paths>({
      baseUrl: `${origin}/v1/workspaces/${encodeURIComponent(config.workspaceId)}`,
      headers: config.headers,
      fetch: config.fetch,
    });
  }

  async request(
    method: string,
    path: string,
    init: { path?: Record<string, string>; query?: object; body?: unknown; parseAs?: "json" | "arrayBuffer"; options?: RequestOptions }
  ): Promise<unknown> {
    const call = (this.raw as unknown as Record<string, (url: string, init: object) => Promise<{ data?: unknown; error?: unknown; response: Response }>>)[method.toUpperCase()];
    const { data, error, response } = await call(path, {
      params: { path: init.path, query: init.query },
      body: init.body,
      parseAs: init.parseAs ?? "json",
      headers: init.options?.headers,
      signal: init.options?.signal,
    });
    if (!response.ok) throw new PleaxyError(response, error);
    return data;
  }
}
