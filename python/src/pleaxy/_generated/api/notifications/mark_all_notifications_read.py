from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mark_all_notifications_read_audience import (
    MarkAllNotificationsReadAudience,
)
from ...models.mark_all_notifications_read_result import MarkAllNotificationsReadResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    audience: MarkAllNotificationsReadAudience,
    cursor: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_audience: str = audience
    params["audience"] = json_audience

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/notifications/read-all",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MarkAllNotificationsReadResult]:
    if response.status_code == 201:
        response_201 = MarkAllNotificationsReadResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MarkAllNotificationsReadResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: MarkAllNotificationsReadAudience,
    cursor: Union[Unset, str] = UNSET,
) -> Response[MarkAllNotificationsReadResult]:
    """[Both] Mark all notifications as read

    Args:
        audience (MarkAllNotificationsReadAudience):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkAllNotificationsReadResult]
    """

    kwargs = _get_kwargs(
        audience=audience,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: MarkAllNotificationsReadAudience,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[MarkAllNotificationsReadResult]:
    """[Both] Mark all notifications as read

    Args:
        audience (MarkAllNotificationsReadAudience):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkAllNotificationsReadResult
    """

    return sync_detailed(
        client=client,
        audience=audience,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: MarkAllNotificationsReadAudience,
    cursor: Union[Unset, str] = UNSET,
) -> Response[MarkAllNotificationsReadResult]:
    """[Both] Mark all notifications as read

    Args:
        audience (MarkAllNotificationsReadAudience):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkAllNotificationsReadResult]
    """

    kwargs = _get_kwargs(
        audience=audience,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    audience: MarkAllNotificationsReadAudience,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[MarkAllNotificationsReadResult]:
    """[Both] Mark all notifications as read

    Args:
        audience (MarkAllNotificationsReadAudience):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkAllNotificationsReadResult
    """

    return (
        await asyncio_detailed(
            client=client,
            audience=audience,
            cursor=cursor,
        )
    ).parsed
