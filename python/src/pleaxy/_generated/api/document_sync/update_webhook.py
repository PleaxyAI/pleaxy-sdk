from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_webhook_input import UpdateWebhookInput
from ...models.webhook_endpoint_view import WebhookEndpointView
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    body: UpdateWebhookInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/webhooks/{webhook_id}".format(
            webhook_id=webhook_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhookEndpointView]:
    if response.status_code == 200:
        response_200 = WebhookEndpointView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhookEndpointView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWebhookInput,
) -> Response[WebhookEndpointView]:
    """[Both, admin] Change an endpoint's url, description or events, or pause and resume it with enabled.
    Resuming clears its count of failed deliveries.

    Args:
        webhook_id (str):
        body (UpdateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointView]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWebhookInput,
) -> Optional[WebhookEndpointView]:
    """[Both, admin] Change an endpoint's url, description or events, or pause and resume it with enabled.
    Resuming clears its count of failed deliveries.

    Args:
        webhook_id (str):
        body (UpdateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointView
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWebhookInput,
) -> Response[WebhookEndpointView]:
    """[Both, admin] Change an endpoint's url, description or events, or pause and resume it with enabled.
    Resuming clears its count of failed deliveries.

    Args:
        webhook_id (str):
        body (UpdateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointView]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWebhookInput,
) -> Optional[WebhookEndpointView]:
    """[Both, admin] Change an endpoint's url, description or events, or pause and resume it with enabled.
    Resuming clears its count of failed deliveries.

    Args:
        webhook_id (str):
        body (UpdateWebhookInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointView
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            body=body,
        )
    ).parsed
