from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_invoice_counterparties_result import ListInvoiceCounterpartiesResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_connection: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["perConnection"] = per_connection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/invoices/counterparties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListInvoiceCounterpartiesResult]:
    if response.status_code == 200:
        response_200 = ListInvoiceCounterpartiesResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListInvoiceCounterpartiesResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    per_connection: Union[Unset, str] = UNSET,
) -> Response[ListInvoiceCounterpartiesResult]:
    """[Both] Active counterparties the caller can invoice through POST .../invoices with a connectionId -
    connection id, display name, the buyer's currency, and the open POs between exactly that pair; a
    Supplier caller also gets the buyer's regionName. One row per counterparty; a Buyer caller can pass
    ?perConnection=true to list every approved connection instead, each with approvedAt, feedReadiness
    and the feed's figures (feedAcceptedCount, feedLastAcceptedAt, feedValidCount, feedLastValidAt) and,
    when a supplier has several, multipleConnections. Without ?perConnection a Buyer caller also gets
    its off-platform suppliers: any supplier in its list with no Pleaxy account yet, invited or not
    (offPlatform: true, cloudProvider for a cloud provider, no POs). For those, currency is only the
    default: the invoice takes its own currency. Human session only.

    Args:
        per_connection (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInvoiceCounterpartiesResult]
    """

    kwargs = _get_kwargs(
        per_connection=per_connection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    per_connection: Union[Unset, str] = UNSET,
) -> Optional[ListInvoiceCounterpartiesResult]:
    """[Both] Active counterparties the caller can invoice through POST .../invoices with a connectionId -
    connection id, display name, the buyer's currency, and the open POs between exactly that pair; a
    Supplier caller also gets the buyer's regionName. One row per counterparty; a Buyer caller can pass
    ?perConnection=true to list every approved connection instead, each with approvedAt, feedReadiness
    and the feed's figures (feedAcceptedCount, feedLastAcceptedAt, feedValidCount, feedLastValidAt) and,
    when a supplier has several, multipleConnections. Without ?perConnection a Buyer caller also gets
    its off-platform suppliers: any supplier in its list with no Pleaxy account yet, invited or not
    (offPlatform: true, cloudProvider for a cloud provider, no POs). For those, currency is only the
    default: the invoice takes its own currency. Human session only.

    Args:
        per_connection (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInvoiceCounterpartiesResult
    """

    return sync_detailed(
        client=client,
        per_connection=per_connection,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    per_connection: Union[Unset, str] = UNSET,
) -> Response[ListInvoiceCounterpartiesResult]:
    """[Both] Active counterparties the caller can invoice through POST .../invoices with a connectionId -
    connection id, display name, the buyer's currency, and the open POs between exactly that pair; a
    Supplier caller also gets the buyer's regionName. One row per counterparty; a Buyer caller can pass
    ?perConnection=true to list every approved connection instead, each with approvedAt, feedReadiness
    and the feed's figures (feedAcceptedCount, feedLastAcceptedAt, feedValidCount, feedLastValidAt) and,
    when a supplier has several, multipleConnections. Without ?perConnection a Buyer caller also gets
    its off-platform suppliers: any supplier in its list with no Pleaxy account yet, invited or not
    (offPlatform: true, cloudProvider for a cloud provider, no POs). For those, currency is only the
    default: the invoice takes its own currency. Human session only.

    Args:
        per_connection (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInvoiceCounterpartiesResult]
    """

    kwargs = _get_kwargs(
        per_connection=per_connection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    per_connection: Union[Unset, str] = UNSET,
) -> Optional[ListInvoiceCounterpartiesResult]:
    """[Both] Active counterparties the caller can invoice through POST .../invoices with a connectionId -
    connection id, display name, the buyer's currency, and the open POs between exactly that pair; a
    Supplier caller also gets the buyer's regionName. One row per counterparty; a Buyer caller can pass
    ?perConnection=true to list every approved connection instead, each with approvedAt, feedReadiness
    and the feed's figures (feedAcceptedCount, feedLastAcceptedAt, feedValidCount, feedLastValidAt) and,
    when a supplier has several, multipleConnections. Without ?perConnection a Buyer caller also gets
    its off-platform suppliers: any supplier in its list with no Pleaxy account yet, invited or not
    (offPlatform: true, cloudProvider for a cloud provider, no POs). For those, currency is only the
    default: the invoice takes its own currency. Human session only.

    Args:
        per_connection (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInvoiceCounterpartiesResult
    """

    return (
        await asyncio_detailed(
            client=client,
            per_connection=per_connection,
        )
    ).parsed
