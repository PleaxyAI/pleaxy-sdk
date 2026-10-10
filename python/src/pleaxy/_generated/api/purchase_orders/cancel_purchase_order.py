from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_purchase_order_input import CancelPurchaseOrderInput
from ...models.purchase_order import PurchaseOrder
from ...types import Response


def _get_kwargs(
    po_id: str,
    *,
    body: CancelPurchaseOrderInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/cancel".format(
            po_id=po_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseOrder]:
    if response.status_code == 201:
        response_201 = PurchaseOrder.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseOrder]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelPurchaseOrderInput,
) -> Response[PurchaseOrder]:
    """[Buyer] Cancel a purchase order

    Args:
        po_id (str):
        body (CancelPurchaseOrderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrder]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelPurchaseOrderInput,
) -> Optional[PurchaseOrder]:
    """[Buyer] Cancel a purchase order

    Args:
        po_id (str):
        body (CancelPurchaseOrderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrder
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelPurchaseOrderInput,
) -> Response[PurchaseOrder]:
    """[Buyer] Cancel a purchase order

    Args:
        po_id (str):
        body (CancelPurchaseOrderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrder]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelPurchaseOrderInput,
) -> Optional[PurchaseOrder]:
    """[Buyer] Cancel a purchase order

    Args:
        po_id (str):
        body (CancelPurchaseOrderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrder
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            body=body,
        )
    ).parsed
