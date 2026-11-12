from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_buyer_view import InvoiceBuyerView
from ...models.invoice_supplier_view import InvoiceSupplierView
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    application_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/invoices/{invoice_id}/credit-applications/{application_id}".format(
            invoice_id=invoice_id,
            application_id=application_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["InvoiceBuyerView", "InvoiceSupplierView"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_remove_credit_application_result_type_0 = (
                    InvoiceBuyerView.from_dict(data)
                )

                return componentsschemas_remove_credit_application_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_remove_credit_application_result_type_1 = (
                InvoiceSupplierView.from_dict(data)
            )

            return componentsschemas_remove_credit_application_result_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
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
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Take a credit back off an invoice that isn't exported or paid. It goes back to its credit
    note.

    Args:
        invoice_id (str):
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Take a credit back off an invoice that isn't exported or paid. It goes back to its credit
    note.

    Args:
        invoice_id (str):
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
    """

    return sync_detailed(
        invoice_id=invoice_id,
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Take a credit back off an invoice that isn't exported or paid. It goes back to its credit
    note.

    Args:
        invoice_id (str):
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['InvoiceBuyerView', 'InvoiceSupplierView']]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union["InvoiceBuyerView", "InvoiceSupplierView"]]:
    """[Buyer] Take a credit back off an invoice that isn't exported or paid. It goes back to its credit
    note.

    Args:
        invoice_id (str):
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['InvoiceBuyerView', 'InvoiceSupplierView']
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            application_id=application_id,
            client=client,
        )
    ).parsed
