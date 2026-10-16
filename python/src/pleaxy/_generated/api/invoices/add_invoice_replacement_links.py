from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_invoice_replacement_links_result import (
    AddInvoiceReplacementLinksResult,
)
from ...models.add_replacement_links_input import AddReplacementLinksInput
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    body: AddReplacementLinksInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/replaces".format(
            invoice_id=invoice_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddInvoiceReplacementLinksResult]:
    if response.status_code == 200:
        response_200 = AddInvoiceReplacementLinksResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddInvoiceReplacementLinksResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddReplacementLinksInput,
) -> Response[AddInvoiceReplacementLinksResult]:
    """[Buyer] Name the invoices this invoice replaces (credit and rebill, credit notes spec §20), when
    that wasn't known as it was entered: { invoiceIds }, 1–20 invoices or debit notes from the same
    supplier. Each original then lists it in replacedByInvoiceIds; links already there are kept. 404
    REPLACES_NOT_FOUND, 400 REPLACES_INVALID, 409 REPLACEMENT_CHANGED.

    Args:
        invoice_id (str):
        body (AddReplacementLinksInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddInvoiceReplacementLinksResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddReplacementLinksInput,
) -> Optional[AddInvoiceReplacementLinksResult]:
    """[Buyer] Name the invoices this invoice replaces (credit and rebill, credit notes spec §20), when
    that wasn't known as it was entered: { invoiceIds }, 1–20 invoices or debit notes from the same
    supplier. Each original then lists it in replacedByInvoiceIds; links already there are kept. 404
    REPLACES_NOT_FOUND, 400 REPLACES_INVALID, 409 REPLACEMENT_CHANGED.

    Args:
        invoice_id (str):
        body (AddReplacementLinksInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddInvoiceReplacementLinksResult
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddReplacementLinksInput,
) -> Response[AddInvoiceReplacementLinksResult]:
    """[Buyer] Name the invoices this invoice replaces (credit and rebill, credit notes spec §20), when
    that wasn't known as it was entered: { invoiceIds }, 1–20 invoices or debit notes from the same
    supplier. Each original then lists it in replacedByInvoiceIds; links already there are kept. 404
    REPLACES_NOT_FOUND, 400 REPLACES_INVALID, 409 REPLACEMENT_CHANGED.

    Args:
        invoice_id (str):
        body (AddReplacementLinksInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddInvoiceReplacementLinksResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddReplacementLinksInput,
) -> Optional[AddInvoiceReplacementLinksResult]:
    """[Buyer] Name the invoices this invoice replaces (credit and rebill, credit notes spec §20), when
    that wasn't known as it was entered: { invoiceIds }, 1–20 invoices or debit notes from the same
    supplier. Each original then lists it in replacedByInvoiceIds; links already there are kept. 404
    REPLACES_NOT_FOUND, 400 REPLACES_INVALID, 409 REPLACEMENT_CHANGED.

    Args:
        invoice_id (str):
        body (AddReplacementLinksInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddInvoiceReplacementLinksResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
