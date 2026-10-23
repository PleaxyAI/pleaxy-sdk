from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_purchase_order_document_format import (
    GetPurchaseOrderDocumentFormat,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    format_: Union[Unset, GetPurchaseOrderDocumentFormat] = UNSET,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["format"] = json_format_

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/purchase-orders/{po_id}/document".format(
            po_id=po_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
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
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetPurchaseOrderDocumentFormat] = UNSET,
    buyer: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[Both] An issued purchase order as a document another system takes in: ?format=cxml (the default: a
    cXML OrderRequest, type new, update from version 2, delete once canceled) or ?format=ubl (a UBL 2.1
    Order, or an OrderCancellation once canceled). The supplier's copy whoever asks, as
    GetPurchaseOrderPdf. Takes the same ?buyer= as GetPurchaseOrder. 409 ORDER_NOT_ISSUED for a draft,
    an order in approval or a rejected one.

    Args:
        po_id (str):
        format_ (Union[Unset, GetPurchaseOrderDocumentFormat]):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        format_=format_,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetPurchaseOrderDocumentFormat] = UNSET,
    buyer: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[Both] An issued purchase order as a document another system takes in: ?format=cxml (the default: a
    cXML OrderRequest, type new, update from version 2, delete once canceled) or ?format=ubl (a UBL 2.1
    Order, or an OrderCancellation once canceled). The supplier's copy whoever asks, as
    GetPurchaseOrderPdf. Takes the same ?buyer= as GetPurchaseOrder. 409 ORDER_NOT_ISSUED for a draft,
    an order in approval or a rejected one.

    Args:
        po_id (str):
        format_ (Union[Unset, GetPurchaseOrderDocumentFormat]):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        format_=format_,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
