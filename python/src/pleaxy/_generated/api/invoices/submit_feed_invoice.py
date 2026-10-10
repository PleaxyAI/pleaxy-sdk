from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_feed_invoice_input import CreateFeedInvoiceInput
from ...models.invoice_supplier_view import InvoiceSupplierView
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: CreateFeedInvoiceInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/connections/{connection_id}".format(
            connection_id=connection_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InvoiceSupplierView]:
    if response.status_code == 201:
        response_201 = InvoiceSupplierView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InvoiceSupplierView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Response[InvoiceSupplierView]:
    """[Supplier] Submit an invoice to one connected buyer from an automated feed (JSON, UBL 2.1 or cXML).
    API key with the invoices:feed scope only; the buyer must turn on automated invoices for the
    connection.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSupplierView]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Optional[InvoiceSupplierView]:
    """[Supplier] Submit an invoice to one connected buyer from an automated feed (JSON, UBL 2.1 or cXML).
    API key with the invoices:feed scope only; the buyer must turn on automated invoices for the
    connection.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSupplierView
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Response[InvoiceSupplierView]:
    """[Supplier] Submit an invoice to one connected buyer from an automated feed (JSON, UBL 2.1 or cXML).
    API key with the invoices:feed scope only; the buyer must turn on automated invoices for the
    connection.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceSupplierView]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFeedInvoiceInput,
) -> Optional[InvoiceSupplierView]:
    """[Supplier] Submit an invoice to one connected buyer from an automated feed (JSON, UBL 2.1 or cXML).
    API key with the invoices:feed scope only; the buyer must turn on automated invoices for the
    connection.

    Args:
        connection_id (str):
        body (CreateFeedInvoiceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceSupplierView
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
        )
    ).parsed
