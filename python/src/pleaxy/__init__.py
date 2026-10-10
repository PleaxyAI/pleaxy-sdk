"""Official Python client for the Pleaxy API.

    import os
    import pleaxy

    client = pleaxy.Client(api_key=os.environ["PLEAXY_API_KEY"], workspace_id=os.environ["PLEAXY_WORKSPACE_ID"])
    orders = client.purchase_orders.list_purchase_orders()

Methods are grouped by API area and named after the operations in the API
Reference (CreatePurchaseOrder -> ``client.purchase_orders.create_purchase_order``).
Request and response models are in ``pleaxy.models``. A failed call raises
:class:`PleaxyError`.
"""

from __future__ import annotations

from typing import Any, Optional, Union

import httpx

from . import models
from ._resources import Resources
from ._transport import PleaxyError, Transport, build_client

__all__ = ["Client", "PleaxyError", "models", "DEFAULT_BASE_URL"]
__version__ = "0.1.0"

DEFAULT_BASE_URL = "https://api.pleaxy.ai"


class Client(Resources):
    """The Pleaxy API client, scoped to one workspace.

    Args:
        workspace_id: Company profile → Workspace ID in the Pleaxy console, e.g. ``reg_01k5x8p9j3q7vn2mhb4tzc6rde.buyer``.
        api_key: An API key, ``<keyId>.<secret>``, minted by a workspace administrator. Sent as ``X-Api-Key``.
        access_token: A signed-in session's access token instead, for the few operations that need a person.
        base_url: The API's origin. The client adds ``/v1/workspaces/<workspace_id>``.
        headers: Headers sent with every call.
        timeout: Seconds, or an ``httpx.Timeout``.
        httpx_args: Passed to ``httpx.Client``, e.g. ``{"transport": ...}`` or ``{"proxy": ...}``.
    """

    def __init__(
        self,
        *,
        workspace_id: str,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        headers: Optional[dict[str, str]] = None,
        timeout: Union[float, httpx.Timeout, None] = 30.0,
        httpx_args: Optional[dict[str, Any]] = None,
    ) -> None:
        self.http = build_client(
            workspace_id=workspace_id,
            api_key=api_key,
            access_token=access_token,
            base_url=base_url,
            headers=headers,
            timeout=timeout,
            httpx_args=httpx_args,
        )
        super().__init__(Transport(self.http))

    def close(self) -> None:
        self.http.get_httpx_client().close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
