from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_po_line_suggestions import AiPoLineSuggestions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    invoicer_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["invoicerId"] = invoicer_id

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-spend/po-lines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiPoLineSuggestions]:
    if response.status_code == 200:
        response_200 = AiPoLineSuggestions.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiPoLineSuggestions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
) -> Response[AiPoLineSuggestions]:
    """[Buyer] Purchase order lines for one invoicer's AI usage in a period (default the last closed
    month): one per model and meter, last month's volume rounded up, priced at the active contract
    term's rate (or its discount off list), else the list price today, else what the month was billed at
    - with priceSource saying which. Nothing is saved: the order form or the Assistant raises the PO.
    'view' on purchase orders.

    Args:
        invoicer_id (Union[Unset, str]):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiPoLineSuggestions]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
) -> Optional[AiPoLineSuggestions]:
    """[Buyer] Purchase order lines for one invoicer's AI usage in a period (default the last closed
    month): one per model and meter, last month's volume rounded up, priced at the active contract
    term's rate (or its discount off list), else the list price today, else what the month was billed at
    - with priceSource saying which. Nothing is saved: the order form or the Assistant raises the PO.
    'view' on purchase orders.

    Args:
        invoicer_id (Union[Unset, str]):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiPoLineSuggestions
    """

    return sync_detailed(
        client=client,
        invoicer_id=invoicer_id,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
) -> Response[AiPoLineSuggestions]:
    """[Buyer] Purchase order lines for one invoicer's AI usage in a period (default the last closed
    month): one per model and meter, last month's volume rounded up, priced at the active contract
    term's rate (or its discount off list), else the list price today, else what the month was billed at
    - with priceSource saying which. Nothing is saved: the order form or the Assistant raises the PO.
    'view' on purchase orders.

    Args:
        invoicer_id (Union[Unset, str]):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiPoLineSuggestions]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
) -> Optional[AiPoLineSuggestions]:
    """[Buyer] Purchase order lines for one invoicer's AI usage in a period (default the last closed
    month): one per model and meter, last month's volume rounded up, priced at the active contract
    term's rate (or its discount off list), else the list price today, else what the month was billed at
    - with priceSource saying which. Nothing is saved: the order form or the Assistant raises the PO.
    'view' on purchase orders.

    Args:
        invoicer_id (Union[Unset, str]):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiPoLineSuggestions
    """

    return (
        await asyncio_detailed(
            client=client,
            invoicer_id=invoicer_id,
            period=period,
        )
    ).parsed
