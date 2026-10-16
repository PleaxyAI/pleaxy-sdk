from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_payment_input import RecordPaymentInput
from ...models.record_payment_result import RecordPaymentResult
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    body: RecordPaymentInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/payment-record".format(
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
) -> Optional[RecordPaymentResult]:
    if response.status_code == 201:
        response_201 = RecordPaymentResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RecordPaymentResult]:
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
    body: RecordPaymentInput,
) -> Response[RecordPaymentResult]:
    """[Buyer] Record a payment the buyer already made outside Pleaxy, in full: { method:
    ach|wire|check|card|other, paymentDate: YYYY-MM-DD, reference }, optionally with a remittance for
    the supplier: { remittance: { note?, file?: { fileId, fileName } } } (see SendRemittance). Pleaxy
    moves no money and doesn't check the payment happened; the supplier is notified and gets a
    remittance advice marked as recorded by the buyer. The date can't be later than today in the
    workspace's time zone or before the invoice date. An amount is refused (400). Repeating the same
    details returns 200 with alreadyRecorded: true; different details are 409 PAYMENT_ALREADY_RECORDED.
    A replaced invoice its credit notes don't cover in full is 409 REPLACED_UNCREDITED until you send
    confirmReplaced: true: paying it as well as its replacement pays twice. Human session only: an API
    key gets 403 HUMAN_SESSION_REQUIRED.

    Args:
        invoice_id (str):
        body (RecordPaymentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordPaymentResult]
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
    body: RecordPaymentInput,
) -> Optional[RecordPaymentResult]:
    """[Buyer] Record a payment the buyer already made outside Pleaxy, in full: { method:
    ach|wire|check|card|other, paymentDate: YYYY-MM-DD, reference }, optionally with a remittance for
    the supplier: { remittance: { note?, file?: { fileId, fileName } } } (see SendRemittance). Pleaxy
    moves no money and doesn't check the payment happened; the supplier is notified and gets a
    remittance advice marked as recorded by the buyer. The date can't be later than today in the
    workspace's time zone or before the invoice date. An amount is refused (400). Repeating the same
    details returns 200 with alreadyRecorded: true; different details are 409 PAYMENT_ALREADY_RECORDED.
    A replaced invoice its credit notes don't cover in full is 409 REPLACED_UNCREDITED until you send
    confirmReplaced: true: paying it as well as its replacement pays twice. Human session only: an API
    key gets 403 HUMAN_SESSION_REQUIRED.

    Args:
        invoice_id (str):
        body (RecordPaymentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordPaymentResult
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
    body: RecordPaymentInput,
) -> Response[RecordPaymentResult]:
    """[Buyer] Record a payment the buyer already made outside Pleaxy, in full: { method:
    ach|wire|check|card|other, paymentDate: YYYY-MM-DD, reference }, optionally with a remittance for
    the supplier: { remittance: { note?, file?: { fileId, fileName } } } (see SendRemittance). Pleaxy
    moves no money and doesn't check the payment happened; the supplier is notified and gets a
    remittance advice marked as recorded by the buyer. The date can't be later than today in the
    workspace's time zone or before the invoice date. An amount is refused (400). Repeating the same
    details returns 200 with alreadyRecorded: true; different details are 409 PAYMENT_ALREADY_RECORDED.
    A replaced invoice its credit notes don't cover in full is 409 REPLACED_UNCREDITED until you send
    confirmReplaced: true: paying it as well as its replacement pays twice. Human session only: an API
    key gets 403 HUMAN_SESSION_REQUIRED.

    Args:
        invoice_id (str):
        body (RecordPaymentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordPaymentResult]
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
    body: RecordPaymentInput,
) -> Optional[RecordPaymentResult]:
    """[Buyer] Record a payment the buyer already made outside Pleaxy, in full: { method:
    ach|wire|check|card|other, paymentDate: YYYY-MM-DD, reference }, optionally with a remittance for
    the supplier: { remittance: { note?, file?: { fileId, fileName } } } (see SendRemittance). Pleaxy
    moves no money and doesn't check the payment happened; the supplier is notified and gets a
    remittance advice marked as recorded by the buyer. The date can't be later than today in the
    workspace's time zone or before the invoice date. An amount is refused (400). Repeating the same
    details returns 200 with alreadyRecorded: true; different details are 409 PAYMENT_ALREADY_RECORDED.
    A replaced invoice its credit notes don't cover in full is 409 REPLACED_UNCREDITED until you send
    confirmReplaced: true: paying it as well as its replacement pays twice. Human session only: an API
    key gets 403 HUMAN_SESSION_REQUIRED.

    Args:
        invoice_id (str):
        body (RecordPaymentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordPaymentResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
