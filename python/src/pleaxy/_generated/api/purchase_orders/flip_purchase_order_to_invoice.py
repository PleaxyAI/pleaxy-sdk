from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_order_supplier_view import PurchaseOrderSupplierView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/flip-to-invoice".format(
            po_id=po_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseOrderSupplierView]:
    if response.status_code == 201:
        response_201 = PurchaseOrderSupplierView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseOrderSupplierView]:
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
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderSupplierView]:
    """[Supplier] Convert an approved purchase order into an invoice. When two buyers issued the same PO
    id, add ?buyer=<buyer Workspace ID> (409 PO_ID_AMBIGUOUS otherwise).

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderSupplierView]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderSupplierView]:
    """[Supplier] Convert an approved purchase order into an invoice. When two buyers issued the same PO
    id, add ?buyer=<buyer Workspace ID> (409 PO_ID_AMBIGUOUS otherwise).

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderSupplierView
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderSupplierView]:
    """[Supplier] Convert an approved purchase order into an invoice. When two buyers issued the same PO
    id, add ?buyer=<buyer Workspace ID> (409 PO_ID_AMBIGUOUS otherwise).

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderSupplierView]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderSupplierView]:
    """[Supplier] Convert an approved purchase order into an invoice. When two buyers issued the same PO
    id, add ?buyer=<buyer Workspace ID> (409 PO_ID_AMBIGUOUS otherwise).

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderSupplierView
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            buyer=buyer,
        )
    ).parsed
