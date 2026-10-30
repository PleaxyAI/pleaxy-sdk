from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_cost_centers_response import AiCostCentersResponse
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
        "url": "/ai-spend/cost-centers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiCostCentersResponse]:
    if response.status_code == 200:
        response_200 = AiCostCentersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiCostCentersResponse]:
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
) -> Response[AiCostCentersResponse]:
    """[Buyer] Each cost center's budget, committed and actual (budget control's figures) with the month's
    attributed AI usage as accruing and its forecast, in the budget's currency, the percent with the
    forecast, and the alert threshold sent; plus what is unattributed. 'view' on purchase orders.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiCostCentersResponse]
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
) -> Optional[AiCostCentersResponse]:
    """[Buyer] Each cost center's budget, committed and actual (budget control's figures) with the month's
    attributed AI usage as accruing and its forecast, in the budget's currency, the percent with the
    forecast, and the alert threshold sent; plus what is unattributed. 'view' on purchase orders.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiCostCentersResponse
    """

    return sync_detailed(
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[AiCostCentersResponse]:
    """[Buyer] Each cost center's budget, committed and actual (budget control's figures) with the month's
    attributed AI usage as accruing and its forecast, in the budget's currency, the percent with the
    forecast, and the alert threshold sent; plus what is unattributed. 'view' on purchase orders.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiCostCentersResponse]
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
) -> Optional[AiCostCentersResponse]:
    """[Buyer] Each cost center's budget, committed and actual (budget control's figures) with the month's
    attributed AI usage as accruing and its forecast, in the budget's currency, the percent with the
    forecast, and the alert threshold sent; plus what is unattributed. 'view' on purchase orders.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiCostCentersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
        )
    ).parsed
