from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_rates_view import ExchangeRatesView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    currency: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/exchange-rates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExchangeRatesView]:
    if response.status_code == 200:
        response_200 = ExchangeRatesView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExchangeRatesView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
) -> Response[ExchangeRatesView]:
    """[Buyer] The currencies this workspace's orders, invoices and suppliers use, each with today's
    reference rate into your currency. `?currency=` adds one more currency's row. Used only for approval
    and spend checks; amounts are never converted. Signed-in session only: the rate provider's terms
    don't allow programmatic access to its rates. Rates by Exchange Rate API.

    Args:
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRatesView]
    """

    kwargs = _get_kwargs(
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
) -> Optional[ExchangeRatesView]:
    """[Buyer] The currencies this workspace's orders, invoices and suppliers use, each with today's
    reference rate into your currency. `?currency=` adds one more currency's row. Used only for approval
    and spend checks; amounts are never converted. Signed-in session only: the rate provider's terms
    don't allow programmatic access to its rates. Rates by Exchange Rate API.

    Args:
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRatesView
    """

    return sync_detailed(
        client=client,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
) -> Response[ExchangeRatesView]:
    """[Buyer] The currencies this workspace's orders, invoices and suppliers use, each with today's
    reference rate into your currency. `?currency=` adds one more currency's row. Used only for approval
    and spend checks; amounts are never converted. Signed-in session only: the rate provider's terms
    don't allow programmatic access to its rates. Rates by Exchange Rate API.

    Args:
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRatesView]
    """

    kwargs = _get_kwargs(
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    currency: Union[Unset, str] = UNSET,
) -> Optional[ExchangeRatesView]:
    """[Buyer] The currencies this workspace's orders, invoices and suppliers use, each with today's
    reference rate into your currency. `?currency=` adds one more currency's row. Used only for approval
    and spend checks; amounts are never converted. Signed-in session only: the rate provider's terms
    don't allow programmatic access to its rates. Rates by Exchange Rate API.

    Args:
        currency (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRatesView
    """

    return (
        await asyncio_detailed(
            client=client,
            currency=currency,
        )
    ).parsed
