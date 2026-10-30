from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_spend_response import AiSpendResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["period"] = period

    params["groupBy"] = group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-spend",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiSpendResponse]:
    if response.status_code == 200:
        response_200 = AiSpendResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiSpendResponse]:
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
    group_by: Union[Unset, str] = UNSET,
) -> Response[AiSpendResponse]:
    """[Buyer] AI spend for a period (YYYY-MM, default this month), grouped by invoicer (default), vendor,
    model or costCenter: month to date, forecast, last month and the change, usage by meter, and beside
    each invoicer the open purchase order lines raised to it with what is left. Amounts stay in each
    invoicer's billing currency; totals are one entry per currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):
        group_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendResponse]
    """

    kwargs = _get_kwargs(
        period=period,
        group_by=group_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
) -> Optional[AiSpendResponse]:
    """[Buyer] AI spend for a period (YYYY-MM, default this month), grouped by invoicer (default), vendor,
    model or costCenter: month to date, forecast, last month and the change, usage by meter, and beside
    each invoicer the open purchase order lines raised to it with what is left. Amounts stay in each
    invoicer's billing currency; totals are one entry per currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):
        group_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiSpendResponse
    """

    return sync_detailed(
        client=client,
        period=period,
        group_by=group_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
) -> Response[AiSpendResponse]:
    """[Buyer] AI spend for a period (YYYY-MM, default this month), grouped by invoicer (default), vendor,
    model or costCenter: month to date, forecast, last month and the change, usage by meter, and beside
    each invoicer the open purchase order lines raised to it with what is left. Amounts stay in each
    invoicer's billing currency; totals are one entry per currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):
        group_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendResponse]
    """

    kwargs = _get_kwargs(
        period=period,
        group_by=group_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
) -> Optional[AiSpendResponse]:
    """[Buyer] AI spend for a period (YYYY-MM, default this month), grouped by invoicer (default), vendor,
    model or costCenter: month to date, forecast, last month and the change, usage by meter, and beside
    each invoicer the open purchase order lines raised to it with what is left. Amounts stay in each
    invoicer's billing currency; totals are one entry per currency. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):
        group_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiSpendResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            group_by=group_by,
        )
    ).parsed
