from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_sourcing_event_summary import BuyerSourcingEventSummary
from ...models.list_sourcing_events_status import (
    ListSourcingEventsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: Union[Unset, ListSourcingEventsStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sourcing-events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["BuyerSourcingEventSummary"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BuyerSourcingEventSummary.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["BuyerSourcingEventSummary"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, ListSourcingEventsStatus] = UNSET,
) -> Response[List["BuyerSourcingEventSummary"]]:
    """[Buyer] The workspace's RFQs, newest first, with answer counts and (unless sealed) the lowest total

    Args:
        status (Union[Unset, ListSourcingEventsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuyerSourcingEventSummary']]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, ListSourcingEventsStatus] = UNSET,
) -> Optional[List["BuyerSourcingEventSummary"]]:
    """[Buyer] The workspace's RFQs, newest first, with answer counts and (unless sealed) the lowest total

    Args:
        status (Union[Unset, ListSourcingEventsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BuyerSourcingEventSummary']
    """

    return sync_detailed(
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, ListSourcingEventsStatus] = UNSET,
) -> Response[List["BuyerSourcingEventSummary"]]:
    """[Buyer] The workspace's RFQs, newest first, with answer counts and (unless sealed) the lowest total

    Args:
        status (Union[Unset, ListSourcingEventsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuyerSourcingEventSummary']]
    """

    kwargs = _get_kwargs(
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, ListSourcingEventsStatus] = UNSET,
) -> Optional[List["BuyerSourcingEventSummary"]]:
    """[Buyer] The workspace's RFQs, newest first, with answer counts and (unless sealed) the lowest total

    Args:
        status (Union[Unset, ListSourcingEventsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BuyerSourcingEventSummary']
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
        )
    ).parsed
