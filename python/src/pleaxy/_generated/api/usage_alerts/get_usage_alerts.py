from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.usage_alerts_response import UsageAlertsResponse
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/usage-alerts",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UsageAlertsResponse]:
    if response.status_code == 200:
        response_200 = UsageAlertsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UsageAlertsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UsageAlertsResponse]:
    """[Buyer] Usage anomaly alerts: the workspace's setting and what the rules find right now - an AI
    model, AI invoicer, cloud account or service above its own trend, or the month's projection breaking
    a contract's cap, tier or commitment - each with its figures, its text (titleMessageId/bodyMessageId
    and params) and sentAt when this month's notification went out. Writes nothing. 'view' on suppliers
    or on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsageAlertsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UsageAlertsResponse]:
    """[Buyer] Usage anomaly alerts: the workspace's setting and what the rules find right now - an AI
    model, AI invoicer, cloud account or service above its own trend, or the month's projection breaking
    a contract's cap, tier or commitment - each with its figures, its text (titleMessageId/bodyMessageId
    and params) and sentAt when this month's notification went out. Writes nothing. 'view' on suppliers
    or on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsageAlertsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UsageAlertsResponse]:
    """[Buyer] Usage anomaly alerts: the workspace's setting and what the rules find right now - an AI
    model, AI invoicer, cloud account or service above its own trend, or the month's projection breaking
    a contract's cap, tier or commitment - each with its figures, its text (titleMessageId/bodyMessageId
    and params) and sentAt when this month's notification went out. Writes nothing. 'view' on suppliers
    or on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsageAlertsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UsageAlertsResponse]:
    """[Buyer] Usage anomaly alerts: the workspace's setting and what the rules find right now - an AI
    model, AI invoicer, cloud account or service above its own trend, or the month's projection breaking
    a contract's cap, tier or commitment - each with its figures, its text (titleMessageId/bodyMessageId
    and params) and sentAt when this month's notification went out. Writes nothing. 'view' on suppliers
    or on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsageAlertsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
