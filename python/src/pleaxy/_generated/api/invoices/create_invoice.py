from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_manual_invoice_input import CreateManualInvoiceInput
from ...models.invoice_buyer_view import InvoiceBuyerView
from ...models.invoice_supplier_view import InvoiceSupplierView
from ...types import Response


def _get_kwargs(
    *,
    body: CreateManualInvoiceInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_create_invoice_result_type_0 = (
                    InvoiceBuyerView.from_dict(data)
                )

                return componentsschemas_create_invoice_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_create_invoice_result_type_1 = (
                InvoiceSupplierView.from_dict(data)
            )

            return componentsschemas_create_invoice_result_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateManualInvoiceInput,
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Both] Record an invoice. JSON with connectionId: an invoice for one active counterparty (a buyer
    for one of its suppliers, including an off-platform cloud provider from GET
    .../invoices/counterparties; a supplier for one of its buyers, signed-in session only). The server
    computes the total from the line items, stores it in the buyer's workspace, and whoever entered it
    can't approve, resolve or settle it. cXML or UBL (buyer only): a supplier's document as received.
    JSON with supplier and amount and no connectionId (buyer only): deprecated, accepted until v2. A
    Supplier API key gets 400 SUPPLIER_DIRECT_INVOICE_RETIRED.

    Args:
        body (CreateManualInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
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
    body: CreateManualInvoiceInput,
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Both] Record an invoice. JSON with connectionId: an invoice for one active counterparty (a buyer
    for one of its suppliers, including an off-platform cloud provider from GET
    .../invoices/counterparties; a supplier for one of its buyers, signed-in session only). The server
    computes the total from the line items, stores it in the buyer's workspace, and whoever entered it
    can't approve, resolve or settle it. cXML or UBL (buyer only): a supplier's document as received.
    JSON with supplier and amount and no connectionId (buyer only): deprecated, accepted until v2. A
    Supplier API key gets 400 SUPPLIER_DIRECT_INVOICE_RETIRED.

    Args:
        body (CreateManualInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateManualInvoiceInput,
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Both] Record an invoice. JSON with connectionId: an invoice for one active counterparty (a buyer
    for one of its suppliers, including an off-platform cloud provider from GET
    .../invoices/counterparties; a supplier for one of its buyers, signed-in session only). The server
    computes the total from the line items, stores it in the buyer's workspace, and whoever entered it
    can't approve, resolve or settle it. cXML or UBL (buyer only): a supplier's document as received.
    JSON with supplier and amount and no connectionId (buyer only): deprecated, accepted until v2. A
    Supplier API key gets 400 SUPPLIER_DIRECT_INVOICE_RETIRED.

    Args:
        body (CreateManualInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateManualInvoiceInput,
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Both] Record an invoice. JSON with connectionId: an invoice for one active counterparty (a buyer
    for one of its suppliers, including an off-platform cloud provider from GET
    .../invoices/counterparties; a supplier for one of its buyers, signed-in session only). The server
    computes the total from the line items, stores it in the buyer's workspace, and whoever entered it
    can't approve, resolve or settle it. cXML or UBL (buyer only): a supplier's document as received.
    JSON with supplier and amount and no connectionId (buyer only): deprecated, accepted until v2. A
    Supplier API key gets 400 SUPPLIER_DIRECT_INVOICE_RETIRED.

    Args:
        body (CreateManualInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
