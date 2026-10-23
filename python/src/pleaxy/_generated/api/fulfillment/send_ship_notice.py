from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_ship_notice_input import CreateShipNoticeInput
from ...models.ship_notice import ShipNotice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    body: CreateShipNoticeInput,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/ship-notices".format(
            po_id=po_id,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ShipNotice]:
    if response.status_code == 201:
        response_201 = ShipNotice.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ShipNotice]:
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
    body: CreateShipNoticeInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[ShipNotice]:
    """[Supplier] Tell the buyer a shipment is on its way (an advance ship notice, as a cXML
    ShipNoticeRequest would): { shipmentId, status?: shipped|planned|canceled, shipmentDate?,
    deliveryDate?, carrier?, trackingNumber?, trackingUrl? (https), note?, lines: [{ lineNo, qty }] }.
    Only goods lines (lineType goods) ordered by quantity ship; a service line is confirmed with a
    service entry sheet. Sending a shipmentId again replaces that shipment; status canceled withdraws it
    (404 SHIPMENT_NOT_FOUND if there is none) and needs no lines. The buyer's requester and receiver are
    told of a new shipment or a new status, and the buyer's sync feed gets purchase_order.shipped. Never
    a receipt: the buyer still confirms what arrives. Only an open order (awaiting_fulfillment or
    invoiced), except to withdraw; 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as
    GetPurchaseOrder. An API key needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateShipNoticeInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipNotice]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
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
    body: CreateShipNoticeInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[ShipNotice]:
    """[Supplier] Tell the buyer a shipment is on its way (an advance ship notice, as a cXML
    ShipNoticeRequest would): { shipmentId, status?: shipped|planned|canceled, shipmentDate?,
    deliveryDate?, carrier?, trackingNumber?, trackingUrl? (https), note?, lines: [{ lineNo, qty }] }.
    Only goods lines (lineType goods) ordered by quantity ship; a service line is confirmed with a
    service entry sheet. Sending a shipmentId again replaces that shipment; status canceled withdraws it
    (404 SHIPMENT_NOT_FOUND if there is none) and needs no lines. The buyer's requester and receiver are
    told of a new shipment or a new status, and the buyer's sync feed gets purchase_order.shipped. Never
    a receipt: the buyer still confirms what arrives. Only an open order (awaiting_fulfillment or
    invoiced), except to withdraw; 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as
    GetPurchaseOrder. An API key needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateShipNoticeInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipNotice
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        body=body,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateShipNoticeInput,
    buyer: Union[Unset, str] = UNSET,
) -> Response[ShipNotice]:
    """[Supplier] Tell the buyer a shipment is on its way (an advance ship notice, as a cXML
    ShipNoticeRequest would): { shipmentId, status?: shipped|planned|canceled, shipmentDate?,
    deliveryDate?, carrier?, trackingNumber?, trackingUrl? (https), note?, lines: [{ lineNo, qty }] }.
    Only goods lines (lineType goods) ordered by quantity ship; a service line is confirmed with a
    service entry sheet. Sending a shipmentId again replaces that shipment; status canceled withdraws it
    (404 SHIPMENT_NOT_FOUND if there is none) and needs no lines. The buyer's requester and receiver are
    told of a new shipment or a new status, and the buyer's sync feed gets purchase_order.shipped. Never
    a receipt: the buyer still confirms what arrives. Only an open order (awaiting_fulfillment or
    invoiced), except to withdraw; 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as
    GetPurchaseOrder. An API key needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateShipNoticeInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipNotice]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        body=body,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateShipNoticeInput,
    buyer: Union[Unset, str] = UNSET,
) -> Optional[ShipNotice]:
    """[Supplier] Tell the buyer a shipment is on its way (an advance ship notice, as a cXML
    ShipNoticeRequest would): { shipmentId, status?: shipped|planned|canceled, shipmentDate?,
    deliveryDate?, carrier?, trackingNumber?, trackingUrl? (https), note?, lines: [{ lineNo, qty }] }.
    Only goods lines (lineType goods) ordered by quantity ship; a service line is confirmed with a
    service entry sheet. Sending a shipmentId again replaces that shipment; status canceled withdraws it
    (404 SHIPMENT_NOT_FOUND if there is none) and needs no lines. The buyer's requester and receiver are
    told of a new shipment or a new status, and the buyer's sync feed gets purchase_order.shipped. Never
    a receipt: the buyer still confirms what arrives. Only an open order (awaiting_fulfillment or
    invoiced), except to withdraw; 409 ORDER_NOT_OPEN otherwise. Takes the same ?buyer= as
    GetPurchaseOrder. An API key needs the orders:fulfill scope.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):
        body (CreateShipNoticeInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipNotice
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            body=body,
            buyer=buyer,
        )
    ).parsed
