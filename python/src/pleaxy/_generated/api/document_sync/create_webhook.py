from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_input import CreateWebhookInput
from ...models.create_webhook_result import CreateWebhookResult
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/webhooks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWebhookResult]:
    if response.status_code == 201:
        response_201 = CreateWebhookResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWebhookResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookInput,
) -> Response[CreateWebhookResult]:
    r"""[Both, admin] Add an endpoint: { url, description?, events? }. Every event of those types (all of
    your side's when events is left out) is POSTed to it as JSON - ListSyncEvents' event plus
    workspaceId and documentPath - signed in the Pleaxy-Signature header (t=<unix seconds>,v1=<hex HMAC-
    SHA256 of \"<t>.<body>\">) with the secret returned here, once. A 2xx within 10 seconds is
    delivered; anything else is retried after 1 min, 5 min, 30 min, 2 h, 6 h, 12 h and 24 h, then given
    up. Up to 5 per side. Signed-in administrators only.

    Args:
        body (CreateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookInput,
) -> Optional[CreateWebhookResult]:
    r"""[Both, admin] Add an endpoint: { url, description?, events? }. Every event of those types (all of
    your side's when events is left out) is POSTed to it as JSON - ListSyncEvents' event plus
    workspaceId and documentPath - signed in the Pleaxy-Signature header (t=<unix seconds>,v1=<hex HMAC-
    SHA256 of \"<t>.<body>\">) with the secret returned here, once. A 2xx within 10 seconds is
    delivered; anything else is retried after 1 min, 5 min, 30 min, 2 h, 6 h, 12 h and 24 h, then given
    up. Up to 5 per side. Signed-in administrators only.

    Args:
        body (CreateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookInput,
) -> Response[CreateWebhookResult]:
    r"""[Both, admin] Add an endpoint: { url, description?, events? }. Every event of those types (all of
    your side's when events is left out) is POSTed to it as JSON - ListSyncEvents' event plus
    workspaceId and documentPath - signed in the Pleaxy-Signature header (t=<unix seconds>,v1=<hex HMAC-
    SHA256 of \"<t>.<body>\">) with the secret returned here, once. A 2xx within 10 seconds is
    delivered; anything else is retried after 1 min, 5 min, 30 min, 2 h, 6 h, 12 h and 24 h, then given
    up. Up to 5 per side. Signed-in administrators only.

    Args:
        body (CreateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWebhookResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWebhookInput,
) -> Optional[CreateWebhookResult]:
    r"""[Both, admin] Add an endpoint: { url, description?, events? }. Every event of those types (all of
    your side's when events is left out) is POSTed to it as JSON - ListSyncEvents' event plus
    workspaceId and documentPath - signed in the Pleaxy-Signature header (t=<unix seconds>,v1=<hex HMAC-
    SHA256 of \"<t>.<body>\">) with the secret returned here, once. A 2xx within 10 seconds is
    delivered; anything else is retried after 1 min, 5 min, 30 min, 2 h, 6 h, 12 h and 24 h, then given
    up. Up to 5 per side. Signed-in administrators only.

    Args:
        body (CreateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWebhookResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
