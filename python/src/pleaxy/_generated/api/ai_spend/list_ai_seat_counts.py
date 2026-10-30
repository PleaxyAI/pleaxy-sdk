from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_seat_count import AiSeatCount
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
        "url": "/ai-spend/seats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AiSeatCount"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AiSeatCount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AiSeatCount"]]:
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
) -> Response[List["AiSeatCount"]]:
    """[Buyer] The seat products' active users recorded for a month (default this month): what seat invoice
    lines and seat commitments are held to. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AiSeatCount']]
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
) -> Optional[List["AiSeatCount"]]:
    """[Buyer] The seat products' active users recorded for a month (default this month): what seat invoice
    lines and seat commitments are held to. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AiSeatCount']
    """

    return sync_detailed(
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[List["AiSeatCount"]]:
    """[Buyer] The seat products' active users recorded for a month (default this month): what seat invoice
    lines and seat commitments are held to. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AiSeatCount']]
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
) -> Optional[List["AiSeatCount"]]:
    """[Buyer] The seat products' active users recorded for a month (default this month): what seat invoice
    lines and seat commitments are held to. 'view' on suppliers or on invoices.

    Args:
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AiSeatCount']
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
        )
    ).parsed
