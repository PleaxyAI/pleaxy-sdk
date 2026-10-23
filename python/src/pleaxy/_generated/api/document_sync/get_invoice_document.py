from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_document_format import (
    GetInvoiceDocumentFormat,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    format_: Union[Unset, GetInvoiceDocumentFormat] = UNSET,
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
        "url": "/invoices/{invoice_id}/document".format(
            invoice_id=invoice_id,
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
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetInvoiceDocumentFormat] = UNSET,
    buyer: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[Both] An invoice as a UBL 2.1 Invoice (?format=ubl, the default and only format), for the buyer's
    ERP to book or the supplier's archive: the lines, document-level discounts and charges, tax and
    withholdings, prepayments, the supplier's payment instructions, the PO and contract it bills. The
    supplier's view whoever asks: no matching, findings or approvals. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        format_ (Union[Unset, GetInvoiceDocumentFormat]):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        format_=format_,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetInvoiceDocumentFormat] = UNSET,
    buyer: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[Both] An invoice as a UBL 2.1 Invoice (?format=ubl, the default and only format), for the buyer's
    ERP to book or the supplier's archive: the lines, document-level discounts and charges, tax and
    withholdings, prepayments, the supplier's payment instructions, the PO and contract it bills. The
    supplier's view whoever asks: no matching, findings or approvals. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        format_ (Union[Unset, GetInvoiceDocumentFormat]):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        format_=format_,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
