from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_connection import CloudConnection
from ...models.cloud_connection_page import CloudConnectionPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/cloud-connections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["CloudConnectionPage", List["CloudConnection"]]]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["CloudConnectionPage", List["CloudConnection"]]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_cloud_connections_result_type_0 = (
                    CloudConnectionPage.from_dict(data)
                )

                return componentsschemas_list_cloud_connections_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            componentsschemas_list_cloud_connections_result_type_1 = []
            _componentsschemas_list_cloud_connections_result_type_1 = data
            for (
                componentsschemas_list_cloud_connections_result_type_1_item_data
            ) in _componentsschemas_list_cloud_connections_result_type_1:
                componentsschemas_list_cloud_connections_result_type_1_item = (
                    CloudConnection.from_dict(
                        componentsschemas_list_cloud_connections_result_type_1_item_data
                    )
                )

                componentsschemas_list_cloud_connections_result_type_1.append(
                    componentsschemas_list_cloud_connections_result_type_1_item
                )

            return componentsschemas_list_cloud_connections_result_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["CloudConnectionPage", List["CloudConnection"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union["CloudConnectionPage", List["CloudConnection"]]]:
    """[Buyer] List cloud provider connections. With `limit` (1–200): one page, `{ items, nextCursor? }`,
    oldest first - pass `cursor` back for the next page. Without it: every connection, as before
    (unbounded; a workspace with thousands of bulk-connected accounts should page).

    Args:
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CloudConnectionPage', List['CloudConnection']]]
    """

    kwargs = _get_kwargs(
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
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union["CloudConnectionPage", List["CloudConnection"]]]:
    """[Buyer] List cloud provider connections. With `limit` (1–200): one page, `{ items, nextCursor? }`,
    oldest first - pass `cursor` back for the next page. Without it: every connection, as before
    (unbounded; a workspace with thousands of bulk-connected accounts should page).

    Args:
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CloudConnectionPage', List['CloudConnection']]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union["CloudConnectionPage", List["CloudConnection"]]]:
    """[Buyer] List cloud provider connections. With `limit` (1–200): one page, `{ items, nextCursor? }`,
    oldest first - pass `cursor` back for the next page. Without it: every connection, as before
    (unbounded; a workspace with thousands of bulk-connected accounts should page).

    Args:
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['CloudConnectionPage', List['CloudConnection']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union["CloudConnectionPage", List["CloudConnection"]]]:
    """[Buyer] List cloud provider connections. With `limit` (1–200): one page, `{ items, nextCursor? }`,
    oldest first - pass `cursor` back for the next page. Without it: every connection, as before
    (unbounded; a workspace with thousands of bulk-connected accounts should page).

    Args:
        limit (Union[Unset, str]):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['CloudConnectionPage', List['CloudConnection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
