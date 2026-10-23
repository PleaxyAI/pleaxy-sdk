from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_deliveries_result import ListWebhookDeliveriesResult
from ...types import Response


def _get_kwargs(
    webhook_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/webhooks/{webhook_id}/deliveries".format(
            webhook_id=webhook_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListWebhookDeliveriesResult]:
    if response.status_code == 200:
        response_200 = ListWebhookDeliveriesResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListWebhookDeliveriesResult]:
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
) -> Response[ListWebhookDeliveriesResult]:
    """[Both, admin] An endpoint's last 50 deliveries, newest first: { deliveries: [{ eventId, type,
    status: pending|delivered|failed, attempts, createdAt, nextAttemptAt, lastAttemptAt, lastStatus,
    lastErrorCode, deliveredAt }] }. Kept 30 days.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookDeliveriesResult]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListWebhookDeliveriesResult]:
    """[Both, admin] An endpoint's last 50 deliveries, newest first: { deliveries: [{ eventId, type,
    status: pending|delivered|failed, attempts, createdAt, nextAttemptAt, lastAttemptAt, lastStatus,
    lastErrorCode, deliveredAt }] }. Kept 30 days.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookDeliveriesResult
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ListWebhookDeliveriesResult]:
    """[Both, admin] An endpoint's last 50 deliveries, newest first: { deliveries: [{ eventId, type,
    status: pending|delivered|failed, attempts, createdAt, nextAttemptAt, lastAttemptAt, lastStatus,
    lastErrorCode, deliveredAt }] }. Kept 30 days.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListWebhookDeliveriesResult]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListWebhookDeliveriesResult]:
    """[Both, admin] An endpoint's last 50 deliveries, newest first: { deliveries: [{ eventId, type,
    status: pending|delivered|failed, attempts, createdAt, nextAttemptAt, lastAttemptAt, lastStatus,
    lastErrorCode, deliveredAt }] }. Kept 30 days.

    Args:
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListWebhookDeliveriesResult
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
