from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_type import RequestType
from ...types import Response


def _get_kwargs(
    type_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/request-types/{type_id}".format(
            type_id=type_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequestType]:
    if response.status_code == 200:
        response_200 = RequestType.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequestType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RequestType]:
    """[Buyer] One request type, active or not, with its intake form

    Args:
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestType]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RequestType]:
    """[Buyer] One request type, active or not, with its intake form

    Args:
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestType
    """

    return sync_detailed(
        type_id=type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RequestType]:
    """[Buyer] One request type, active or not, with its intake form

    Args:
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestType]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RequestType]:
    """[Buyer] One request type, active or not, with its intake form

    Args:
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestType
    """

    return (
        await asyncio_detailed(
            type_id=type_id,
            client=client,
        )
    ).parsed
