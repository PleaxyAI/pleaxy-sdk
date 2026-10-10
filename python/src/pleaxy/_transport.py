from __future__ import annotations

import importlib
from typing import Any, Optional, Union

import httpx

from ._generated.client import AuthenticatedClient


class PleaxyError(Exception):
    """Raised for every non-2xx response.

    ``code`` is the API's machine-readable reason when it names one (e.g. ``"PO_ID_AMBIGUOUS"``).
    """

    def __init__(self, response: httpx.Response) -> None:
        self.status: int = response.status_code
        self.response = response
        try:
            self.body: Any = response.json()
        except ValueError:
            self.body = response.text
        error = self.body if isinstance(self.body, dict) else {}
        self.code: Optional[str] = error.get("code")
        message = error.get("message") or (self.body if isinstance(self.body, str) and self.body else response.reason_phrase)
        if isinstance(message, list):
            message = "; ".join(str(m) for m in message)
        super().__init__(f"{self.status} {self.code + ': ' if self.code else ''}{message}")


class Transport:
    def __init__(self, client: AuthenticatedClient) -> None:
        self.client = client

    def call(self, module: str, binary: bool = False, **kwargs: Any) -> Any:
        operation = importlib.import_module(module)
        response = self.client.get_httpx_client().request(**operation._get_kwargs(**kwargs))
        if not response.is_success:
            raise PleaxyError(response)
        if binary:
            return response.content
        return operation._parse_response(client=self.client, response=response)


def build_client(
    *,
    workspace_id: str,
    api_key: Optional[str],
    access_token: Optional[str],
    base_url: str,
    headers: Optional[dict[str, str]],
    timeout: Union[float, httpx.Timeout, None],
    httpx_args: Optional[dict[str, Any]] = None,
) -> AuthenticatedClient:
    if not workspace_id:
        raise ValueError("Pleaxy: workspace_id is required (Company profile → Workspace ID in the Pleaxy console).")
    if not api_key and not access_token:
        raise ValueError("Pleaxy: pass an api_key or an access_token.")
    origin = base_url.rstrip("/")
    return AuthenticatedClient(
        base_url=f"{origin}/v1/workspaces/{httpx.URL(workspace_id).raw_path.decode()}",
        token=api_key or access_token or "",
        prefix="" if api_key else "Bearer",
        auth_header_name="X-Api-Key" if api_key else "Authorization",
        headers=headers or {},
        timeout=httpx.Timeout(timeout) if isinstance(timeout, (int, float)) else timeout,
        httpx_args=httpx_args or {},
    )
