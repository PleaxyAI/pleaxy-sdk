from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_notifications_audience import (
    ListNotificationsAudience,
)
from ...models.notification import Notification
from ...types import UNSET, Response


def _get_kwargs(
    *,
    audience: ListNotificationsAudience,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_audience: str = audience
    params["audience"] = json_audience

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Notification"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Notification.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Notification"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: ListNotificationsAudience,
) -> Response[List["Notification"]]:
    """[Both] List notifications (the 50 most recent)

    Args:
        audience (ListNotificationsAudience):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Notification']]
    """

    kwargs = _get_kwargs(
        audience=audience,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: ListNotificationsAudience,
) -> Optional[List["Notification"]]:
    """[Both] List notifications (the 50 most recent)

    Args:
        audience (ListNotificationsAudience):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Notification']
    """

    return sync_detailed(
        client=client,
        audience=audience,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: ListNotificationsAudience,
) -> Response[List["Notification"]]:
    """[Both] List notifications (the 50 most recent)

    Args:
        audience (ListNotificationsAudience):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Notification']]
    """

    kwargs = _get_kwargs(
        audience=audience,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: ListNotificationsAudience,
) -> Optional[List["Notification"]]:
    """[Both] List notifications (the 50 most recent)

    Args:
        audience (ListNotificationsAudience):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Notification']
    """

    return (
        await asyncio_detailed(
            client=client,
            audience=audience,
        )
    ).parsed
