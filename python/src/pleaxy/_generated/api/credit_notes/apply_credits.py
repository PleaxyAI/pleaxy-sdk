from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_credits_input import ApplyCreditsInput
from ...models.invoice_buyer_view import InvoiceBuyerView
from ...models.invoice_supplier_view import InvoiceSupplierView
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    body: ApplyCreditsInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/credit-applications".format(
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
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_apply_credits_result_type_0 = (
                    InvoiceBuyerView.from_dict(data)
                )

                return componentsschemas_apply_credits_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_apply_credits_result_type_1 = (
                InvoiceSupplierView.from_dict(data)
            )

            return componentsschemas_apply_credits_result_type_1

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
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApplyCreditsInput,
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Apply accepted credit notes to an invoice, all or none, up to what it owes; an approved
    invoice covered in full is marked paid by credit. 409 when credits are settled in your accounting
    system.

    Args:
        invoice_id (str):
        body (ApplyCreditsInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
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
    body: ApplyCreditsInput,
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Apply accepted credit notes to an invoice, all or none, up to what it owes; an approved
    invoice covered in full is marked paid by credit. 409 when credits are settled in your accounting
    system.

    Args:
        invoice_id (str):
        body (ApplyCreditsInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
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
    body: ApplyCreditsInput,
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Apply accepted credit notes to an invoice, all or none, up to what it owes; an approved
    invoice covered in full is marked paid by credit. 409 when credits are settled in your accounting
    system.

    Args:
        invoice_id (str):
        body (ApplyCreditsInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
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
    body: ApplyCreditsInput,
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Apply accepted credit notes to an invoice, all or none, up to what it owes; an approved
    invoice covered in full is marked paid by credit. 409 when credits are settled in your accounting
    system.

    Args:
        invoice_id (str):
        body (ApplyCreditsInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
