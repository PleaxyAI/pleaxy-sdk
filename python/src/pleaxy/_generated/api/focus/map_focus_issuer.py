from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.focus_issuer_view import FocusIssuerView
from ...models.map_focus_issuer_input import MapFocusIssuerInput
from ...types import Response


def _get_kwargs(
    issuer: str,
    *,
    body: MapFocusIssuerInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/focus-sources/issuers/{issuer}".format(
            issuer=issuer,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["FocusIssuerView"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FocusIssuerView.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["FocusIssuerView"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issuer: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MapFocusIssuerInput,
) -> Response[List["FocusIssuerView"]]:
    """[Buyer] Map a FOCUS invoice issuer to one of the workspace's suppliers (supplierConnectionId), or
    forget the mapping (null). 'edit' on invoices.

    Args:
        issuer (str):
        body (MapFocusIssuerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['FocusIssuerView']]
    """

    kwargs = _get_kwargs(
        issuer=issuer,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issuer: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MapFocusIssuerInput,
) -> Optional[List["FocusIssuerView"]]:
    """[Buyer] Map a FOCUS invoice issuer to one of the workspace's suppliers (supplierConnectionId), or
    forget the mapping (null). 'edit' on invoices.

    Args:
        issuer (str):
        body (MapFocusIssuerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['FocusIssuerView']
    """

    return sync_detailed(
        issuer=issuer,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    issuer: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MapFocusIssuerInput,
) -> Response[List["FocusIssuerView"]]:
    """[Buyer] Map a FOCUS invoice issuer to one of the workspace's suppliers (supplierConnectionId), or
    forget the mapping (null). 'edit' on invoices.

    Args:
        issuer (str):
        body (MapFocusIssuerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['FocusIssuerView']]
    """

    kwargs = _get_kwargs(
        issuer=issuer,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issuer: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: MapFocusIssuerInput,
) -> Optional[List["FocusIssuerView"]]:
    """[Buyer] Map a FOCUS invoice issuer to one of the workspace's suppliers (supplierConnectionId), or
    forget the mapping (null). 'edit' on invoices.

    Args:
        issuer (str):
        body (MapFocusIssuerInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['FocusIssuerView']
    """

    return (
        await asyncio_detailed(
            issuer=issuer,
            client=client,
            body=body,
        )
    ).parsed
