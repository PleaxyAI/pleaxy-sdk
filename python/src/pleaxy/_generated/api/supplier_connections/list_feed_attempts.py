from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feed_attempts_page import FeedAttemptsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: str,
    *,
    before: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/supplier-connections/{connection_id}/feed-attempts".format(
            connection_id=connection_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FeedAttemptsPage]:
    if response.status_code == 200:
        response_200 = FeedAttemptsPage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FeedAttemptsPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, str] = UNSET,
) -> Response[FeedAttemptsPage]:
    """[Both] The feed attempt log for one of your connections: every call to its automated-invoice route
    or its validate twin that reached the connection, newest first, 50 a page (`?before=` the last row's
    cursor for the next). Both sides see the same rows. 404 when the connection isn't yours

    Args:
        connection_id (str):
        before (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedAttemptsPage]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, str] = UNSET,
) -> Optional[FeedAttemptsPage]:
    """[Both] The feed attempt log for one of your connections: every call to its automated-invoice route
    or its validate twin that reached the connection, newest first, 50 a page (`?before=` the last row's
    cursor for the next). Both sides see the same rows. 404 when the connection isn't yours

    Args:
        connection_id (str):
        before (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedAttemptsPage
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        before=before,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, str] = UNSET,
) -> Response[FeedAttemptsPage]:
    """[Both] The feed attempt log for one of your connections: every call to its automated-invoice route
    or its validate twin that reached the connection, newest first, 50 a page (`?before=` the last row's
    cursor for the next). Both sides see the same rows. 404 when the connection isn't yours

    Args:
        connection_id (str):
        before (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedAttemptsPage]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, str] = UNSET,
) -> Optional[FeedAttemptsPage]:
    """[Both] The feed attempt log for one of your connections: every call to its automated-invoice route
    or its validate twin that reached the connection, newest first, 50 a page (`?before=` the last row's
    cursor for the next). Both sides see the same rows. 404 when the connection isn't yours

    Args:
        connection_id (str):
        before (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedAttemptsPage
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            before=before,
        )
    ).parsed
