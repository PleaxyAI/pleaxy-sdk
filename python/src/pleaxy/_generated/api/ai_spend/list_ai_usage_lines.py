from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_usage_lines_page import AiUsageLinesPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: Union[Unset, str] = UNSET,
    invoicer_id: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    cost_center: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["period"] = period

    params["invoicerId"] = invoicer_id

    params["vendor"] = vendor

    params["model"] = model

    params["costCenter"] = cost_center

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-spend/lines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiUsageLinesPage]:
    if response.status_code == 200:
        response_200 = AiUsageLinesPage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiUsageLinesPage]:
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
    invoicer_id: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    cost_center: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[AiUsageLinesPage]:
    """[Buyer] The normalised AI usage lines behind the figures, newest day first, one page at a time
    (limit 1-500, default 100; pass nextCursor back as cursor). Filter by invoicerId, vendor, model or
    costCenter. Unmapped usage types keep their raw names with vendor unknown. 'view' on suppliers or on
    invoices.

    Args:
        period (Union[Unset, str]):
        invoicer_id (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiUsageLinesPage]
    """

    kwargs = _get_kwargs(
        period=period,
        invoicer_id=invoicer_id,
        vendor=vendor,
        model=model,
        cost_center=cost_center,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    invoicer_id: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    cost_center: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[AiUsageLinesPage]:
    """[Buyer] The normalised AI usage lines behind the figures, newest day first, one page at a time
    (limit 1-500, default 100; pass nextCursor back as cursor). Filter by invoicerId, vendor, model or
    costCenter. Unmapped usage types keep their raw names with vendor unknown. 'view' on suppliers or on
    invoices.

    Args:
        period (Union[Unset, str]):
        invoicer_id (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiUsageLinesPage
    """

    return sync_detailed(
        client=client,
        period=period,
        invoicer_id=invoicer_id,
        vendor=vendor,
        model=model,
        cost_center=cost_center,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    invoicer_id: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    cost_center: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[AiUsageLinesPage]:
    """[Buyer] The normalised AI usage lines behind the figures, newest day first, one page at a time
    (limit 1-500, default 100; pass nextCursor back as cursor). Filter by invoicerId, vendor, model or
    costCenter. Unmapped usage types keep their raw names with vendor unknown. 'view' on suppliers or on
    invoices.

    Args:
        period (Union[Unset, str]):
        invoicer_id (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiUsageLinesPage]
    """

    kwargs = _get_kwargs(
        period=period,
        invoicer_id=invoicer_id,
        vendor=vendor,
        model=model,
        cost_center=cost_center,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
    invoicer_id: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    cost_center: Union[Unset, str] = UNSET,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[AiUsageLinesPage]:
    """[Buyer] The normalised AI usage lines behind the figures, newest day first, one page at a time
    (limit 1-500, default 100; pass nextCursor back as cursor). Filter by invoicerId, vendor, model or
    costCenter. Unmapped usage types keep their raw names with vendor unknown. 'view' on suppliers or on
    invoices.

    Args:
        period (Union[Unset, str]):
        invoicer_id (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiUsageLinesPage
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            invoicer_id=invoicer_id,
            vendor=vendor,
            model=model,
            cost_center=cost_center,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
