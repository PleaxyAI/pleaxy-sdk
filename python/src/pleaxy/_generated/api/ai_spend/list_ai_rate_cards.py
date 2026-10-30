from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_rate_card_entry import AiRateCardEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    invoicer: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    on: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["invoicer"] = invoicer

    params["vendor"] = vendor

    params["model"] = model

    params["on"] = on

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-rate-cards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AiRateCardEntry"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AiRateCardEntry.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AiRateCardEntry"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    on: Union[Unset, str] = UNSET,
) -> Response[List["AiRateCardEntry"]]:
    """[Buyer] The public list prices Pleaxy keeps for AI models, by invoicer, vendor, model, meter and
    region, with effective dates and the pricing page each was taken from. With on (YYYY-MM-DD), only
    the entry in force that day. A price change is a new entry, never an edit. 'view' on suppliers or on
    invoices.

    Args:
        invoicer (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        on (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AiRateCardEntry']]
    """

    kwargs = _get_kwargs(
        invoicer=invoicer,
        vendor=vendor,
        model=model,
        on=on,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    on: Union[Unset, str] = UNSET,
) -> Optional[List["AiRateCardEntry"]]:
    """[Buyer] The public list prices Pleaxy keeps for AI models, by invoicer, vendor, model, meter and
    region, with effective dates and the pricing page each was taken from. With on (YYYY-MM-DD), only
    the entry in force that day. A price change is a new entry, never an edit. 'view' on suppliers or on
    invoices.

    Args:
        invoicer (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        on (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AiRateCardEntry']
    """

    return sync_detailed(
        client=client,
        invoicer=invoicer,
        vendor=vendor,
        model=model,
        on=on,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    on: Union[Unset, str] = UNSET,
) -> Response[List["AiRateCardEntry"]]:
    """[Buyer] The public list prices Pleaxy keeps for AI models, by invoicer, vendor, model, meter and
    region, with effective dates and the pricing page each was taken from. With on (YYYY-MM-DD), only
    the entry in force that day. A price change is a new entry, never an edit. 'view' on suppliers or on
    invoices.

    Args:
        invoicer (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        on (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AiRateCardEntry']]
    """

    kwargs = _get_kwargs(
        invoicer=invoicer,
        vendor=vendor,
        model=model,
        on=on,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    invoicer: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    model: Union[Unset, str] = UNSET,
    on: Union[Unset, str] = UNSET,
) -> Optional[List["AiRateCardEntry"]]:
    """[Buyer] The public list prices Pleaxy keeps for AI models, by invoicer, vendor, model, meter and
    region, with effective dates and the pricing page each was taken from. With on (YYYY-MM-DD), only
    the entry in force that day. A price change is a new entry, never an edit. 'view' on suppliers or on
    invoices.

    Args:
        invoicer (Union[Unset, str]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        on (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AiRateCardEntry']
    """

    return (
        await asyncio_detailed(
            client=client,
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            on=on,
        )
    ).parsed
