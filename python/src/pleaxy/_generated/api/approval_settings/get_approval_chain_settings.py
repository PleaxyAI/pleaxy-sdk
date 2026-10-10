from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_chain_settings import ApprovalChainSettings
from ...types import Response


def _get_kwargs(
    process: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/approval-chains/{process}".format(
            process=process,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApprovalChainSettings]:
    if response.status_code == 200:
        response_200 = ApprovalChainSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApprovalChainSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApprovalChainSettings]:
    """[Buyer] Get the configured approval chain for a process

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalChainSettings]
    """

    kwargs = _get_kwargs(
        process=process,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApprovalChainSettings]:
    """[Buyer] Get the configured approval chain for a process

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalChainSettings
    """

    return sync_detailed(
        process=process,
        client=client,
    ).parsed


async def asyncio_detailed(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApprovalChainSettings]:
    """[Buyer] Get the configured approval chain for a process

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalChainSettings]
    """

    kwargs = _get_kwargs(
        process=process,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApprovalChainSettings]:
    """[Buyer] Get the configured approval chain for a process

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalChainSettings
    """

    return (
        await asyncio_detailed(
            process=process,
            client=client,
        )
    ).parsed
