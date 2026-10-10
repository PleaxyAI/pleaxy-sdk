from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.discover_azure_scopes_input import DiscoverAzureScopesInput
from ...types import Response


def _get_kwargs(
    *,
    body: DiscoverAzureScopesInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/cloud-connections/azure/discover",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == 201:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiscoverAzureScopesInput,
) -> Response[Any]:
    """[Buyer] Azure, when its connector is on: prove the tenant ID and app (client) ID the setup script
    printed, with an app-only token for this connection's own federated-credential audience, and read
    the given Microsoft Customer Agreement billing account and billing profile with it (the account list
    is empty for an app that holds only Billing profile reader). Only the person who started the setup
    may call it, and it counts against the same attempt limit and cooldown as verify. 404 while Azure is
    demo-only.

    Args:
        body (DiscoverAzureScopesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DiscoverAzureScopesInput,
) -> Response[Any]:
    """[Buyer] Azure, when its connector is on: prove the tenant ID and app (client) ID the setup script
    printed, with an app-only token for this connection's own federated-credential audience, and read
    the given Microsoft Customer Agreement billing account and billing profile with it (the account list
    is empty for an app that holds only Billing profile reader). Only the person who started the setup
    may call it, and it counts against the same attempt limit and cooldown as verify. 404 while Azure is
    demo-only.

    Args:
        body (DiscoverAzureScopesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
