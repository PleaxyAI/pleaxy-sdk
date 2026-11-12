from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_sourcing_event_view import BuyerSourcingEventView
from ...types import Response


def _get_kwargs(
    rfq_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sourcing-events/{rfq_id}".format(
            rfq_id=rfq_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BuyerSourcingEventView]:
    if response.status_code == 200:
        response_200 = BuyerSourcingEventView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BuyerSourcingEventView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BuyerSourcingEventView]:
    """[Buyer] One RFQ. While open and sealed: each invitee's state and when it answered, never prices or
    files

    Args:
        rfq_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerSourcingEventView]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BuyerSourcingEventView]:
    """[Buyer] One RFQ. While open and sealed: each invitee's state and when it answered, never prices or
    files

    Args:
        rfq_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyerSourcingEventView
    """

    return sync_detailed(
        rfq_id=rfq_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BuyerSourcingEventView]:
    """[Buyer] One RFQ. While open and sealed: each invitee's state and when it answered, never prices or
    files

    Args:
        rfq_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerSourcingEventView]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BuyerSourcingEventView]:
    """[Buyer] One RFQ. While open and sealed: each invitee's state and when it answered, never prices or
    files

    Args:
        rfq_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyerSourcingEventView
    """

    return (
        await asyncio_detailed(
            rfq_id=rfq_id,
            client=client,
        )
    ).parsed
