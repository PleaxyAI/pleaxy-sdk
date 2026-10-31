from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_recommendations import AiRecommendations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-spend/recommendations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiRecommendations]:
    if response.status_code == 200:
        response_200 = AiRecommendations.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiRecommendations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[AiRecommendations]:
    """[Buyer] Recommendations: the AI spend no open order covers in a period (default this month) - an
    invoicer with no order raised to it (no_po), or a forecast past what its orders have left (over_po),
    with the gap a new order needs and any draft (draftPoIds) or order waiting on approval
    (pendingPoIds) already raised for it; accounts, the same for whole cloud accounts (all their spend,
    from the provider's current estimate, this month only; an account's AI spend is part of it, so never
    add the two) - and cheaper ways to buy last month's usage: batch (the most moving interactive tokens
    to the batch rate would save), cache (what each further 10% of input read from the cache saves) and
    reserve (GPU-hours used at a steady floor most days, with the GPUs that floor keeps busy; no price,
    the contract decides it). Amounts in each invoicer's currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiRecommendations]
    """

    kwargs = _get_kwargs(
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Optional[AiRecommendations]:
    """[Buyer] Recommendations: the AI spend no open order covers in a period (default this month) - an
    invoicer with no order raised to it (no_po), or a forecast past what its orders have left (over_po),
    with the gap a new order needs and any draft (draftPoIds) or order waiting on approval
    (pendingPoIds) already raised for it; accounts, the same for whole cloud accounts (all their spend,
    from the provider's current estimate, this month only; an account's AI spend is part of it, so never
    add the two) - and cheaper ways to buy last month's usage: batch (the most moving interactive tokens
    to the batch rate would save), cache (what each further 10% of input read from the cache saves) and
    reserve (GPU-hours used at a steady floor most days, with the GPUs that floor keeps busy; no price,
    the contract decides it). Amounts in each invoicer's currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiRecommendations
    """

    return sync_detailed(
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[AiRecommendations]:
    """[Buyer] Recommendations: the AI spend no open order covers in a period (default this month) - an
    invoicer with no order raised to it (no_po), or a forecast past what its orders have left (over_po),
    with the gap a new order needs and any draft (draftPoIds) or order waiting on approval
    (pendingPoIds) already raised for it; accounts, the same for whole cloud accounts (all their spend,
    from the provider's current estimate, this month only; an account's AI spend is part of it, so never
    add the two) - and cheaper ways to buy last month's usage: batch (the most moving interactive tokens
    to the batch rate would save), cache (what each further 10% of input read from the cache saves) and
    reserve (GPU-hours used at a steady floor most days, with the GPUs that floor keeps busy; no price,
    the contract decides it). Amounts in each invoicer's currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiRecommendations]
    """

    kwargs = _get_kwargs(
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Optional[AiRecommendations]:
    """[Buyer] Recommendations: the AI spend no open order covers in a period (default this month) - an
    invoicer with no order raised to it (no_po), or a forecast past what its orders have left (over_po),
    with the gap a new order needs and any draft (draftPoIds) or order waiting on approval
    (pendingPoIds) already raised for it; accounts, the same for whole cloud accounts (all their spend,
    from the provider's current estimate, this month only; an account's AI spend is part of it, so never
    add the two) - and cheaper ways to buy last month's usage: batch (the most moving interactive tokens
    to the batch rate would save), cache (what each further 10% of input read from the cache saves) and
    reserve (GPU-hours used at a steady floor most days, with the GPUs that floor keeps busy; no price,
    the contract decides it). Amounts in each invoicer's currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiRecommendations
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
        )
    ).parsed
