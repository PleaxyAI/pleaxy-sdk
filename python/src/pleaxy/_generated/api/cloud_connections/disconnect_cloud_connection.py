from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_connection_disconnected import CloudConnectionDisconnected
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/cloud-connections/{id}".format(
            id=id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CloudConnectionDisconnected]:
    if response.status_code == 200:
        response_200 = CloudConnectionDisconnected.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CloudConnectionDisconnected]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CloudConnectionDisconnected]:
    """[Buyer] Disconnect a cloud account (logged-in users only, 'edit' on suppliers). Deletes the
    connection with everything Pleaxy stored for it (for Oracle Cloud, its encrypted API key) and
    records who disconnected it; for Oracle Cloud the response names the key fingerprint to delete from
    user pleaxy-billing. A setup still in progress can only be cancelled by the person who started it
    (403 otherwise).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudConnectionDisconnected]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CloudConnectionDisconnected]:
    """[Buyer] Disconnect a cloud account (logged-in users only, 'edit' on suppliers). Deletes the
    connection with everything Pleaxy stored for it (for Oracle Cloud, its encrypted API key) and
    records who disconnected it; for Oracle Cloud the response names the key fingerprint to delete from
    user pleaxy-billing. A setup still in progress can only be cancelled by the person who started it
    (403 otherwise).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudConnectionDisconnected
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CloudConnectionDisconnected]:
    """[Buyer] Disconnect a cloud account (logged-in users only, 'edit' on suppliers). Deletes the
    connection with everything Pleaxy stored for it (for Oracle Cloud, its encrypted API key) and
    records who disconnected it; for Oracle Cloud the response names the key fingerprint to delete from
    user pleaxy-billing. A setup still in progress can only be cancelled by the person who started it
    (403 otherwise).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudConnectionDisconnected]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CloudConnectionDisconnected]:
    """[Buyer] Disconnect a cloud account (logged-in users only, 'edit' on suppliers). Deletes the
    connection with everything Pleaxy stored for it (for Oracle Cloud, its encrypted API key) and
    records who disconnected it; for Oracle Cloud the response names the key fingerprint to delete from
    user pleaxy-billing. A setup still in progress can only be cancelled by the person who started it
    (403 otherwise).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudConnectionDisconnected
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
