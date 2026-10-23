from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_purchase_request_input import CreatePurchaseRequestInput
from ...models.purchase_request import PurchaseRequest
from ...types import Response


def _get_kwargs(
    *,
    body: CreatePurchaseRequestInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-requests",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseRequest]:
    if response.status_code == 201:
        response_201 = PurchaseRequest.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreatePurchaseRequestInput,
) -> Response[PurchaseRequest]:
    """[Buyer] Ask for something: saved as a draft, or submitted for approval with `submit: true`. Any
    workspace member.

    Args:
        body (CreatePurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseRequest]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreatePurchaseRequestInput,
) -> Optional[PurchaseRequest]:
    """[Buyer] Ask for something: saved as a draft, or submitted for approval with `submit: true`. Any
    workspace member.

    Args:
        body (CreatePurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseRequest
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreatePurchaseRequestInput,
) -> Response[PurchaseRequest]:
    """[Buyer] Ask for something: saved as a draft, or submitted for approval with `submit: true`. Any
    workspace member.

    Args:
        body (CreatePurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseRequest]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreatePurchaseRequestInput,
) -> Optional[PurchaseRequest]:
    """[Buyer] Ask for something: saved as a draft, or submitted for approval with `submit: true`. Any
    workspace member.

    Args:
        body (CreatePurchaseRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseRequest
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
