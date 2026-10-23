from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remittance_view import RemittanceView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/invoices/{invoice_id}/remittance".format(
            invoice_id=invoice_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemittanceView]:
    if response.status_code == 200:
        response_200 = RemittanceView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemittanceView]:
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
    buyer: Union[Unset, str] = UNSET,
) -> Response[RemittanceView]:
    """[Both] The payment signal for an invoice, for the supplier's cash application: status
    unpaid|recorded|processing|paid_through_pleaxy|withdrawn, and once paid the method (ach, wire,
    check, card, other; credit or nothing_due when Pleaxy closed it; stripe), paymentDate, reference,
    adviceVersion, what was withheld, netPaid, a payment in another currency, and the remittances the
    buyer sent (notes, proofs of payment: download one with GetRemittanceFile). The same as cXML or UBL:
    GetInvoiceRemittanceDocument. Never who at the buyer recorded it. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemittanceView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[RemittanceView]:
    """[Both] The payment signal for an invoice, for the supplier's cash application: status
    unpaid|recorded|processing|paid_through_pleaxy|withdrawn, and once paid the method (ach, wire,
    check, card, other; credit or nothing_due when Pleaxy closed it; stripe), paymentDate, reference,
    adviceVersion, what was withheld, netPaid, a payment in another currency, and the remittances the
    buyer sent (notes, proofs of payment: download one with GetRemittanceFile). The same as cXML or UBL:
    GetInvoiceRemittanceDocument. Never who at the buyer recorded it. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemittanceView
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[RemittanceView]:
    """[Both] The payment signal for an invoice, for the supplier's cash application: status
    unpaid|recorded|processing|paid_through_pleaxy|withdrawn, and once paid the method (ach, wire,
    check, card, other; credit or nothing_due when Pleaxy closed it; stripe), paymentDate, reference,
    adviceVersion, what was withheld, netPaid, a payment in another currency, and the remittances the
    buyer sent (notes, proofs of payment: download one with GetRemittanceFile). The same as cXML or UBL:
    GetInvoiceRemittanceDocument. Never who at the buyer recorded it. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemittanceView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[RemittanceView]:
    """[Both] The payment signal for an invoice, for the supplier's cash application: status
    unpaid|recorded|processing|paid_through_pleaxy|withdrawn, and once paid the method (ach, wire,
    check, card, other; credit or nothing_due when Pleaxy closed it; stripe), paymentDate, reference,
    adviceVersion, what was withheld, netPaid, a payment in another currency, and the remittances the
    buyer sent (notes, proofs of payment: download one with GetRemittanceFile). The same as cXML or UBL:
    GetInvoiceRemittanceDocument. Never who at the buyer recorded it. Takes the same ?buyer= as
    GetInvoice.

    Args:
        invoice_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemittanceView
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            buyer=buyer,
        )
    ).parsed
