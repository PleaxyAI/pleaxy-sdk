from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_payments_batch_input import RecordPaymentsBatchInput
from ...models.record_payments_result import RecordPaymentsResult
from ...types import Response


def _get_kwargs(
    *,
    body: RecordPaymentsBatchInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/payment-records",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RecordPaymentsResult]:
    if response.status_code == 200:
        response_200 = RecordPaymentsResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RecordPaymentsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RecordPaymentsBatchInput,
) -> Response[RecordPaymentsResult]:
    """[Buyer] Record payments your ERP or bank feed already made outside Pleaxy - wires, checks, ACH, card
    - so each supplier gets its payment notice, remittance advice and sync event without anyone retyping
    it: { payments: [{ invoiceId, method, paymentDate, reference, note?, ...RecordPayment's currency and
    withholding fields }] }, 1-50 per call. Each payment follows RecordPayment's rules and is answered
    on its own: { results: [{ invoiceId, outcome: recorded|already_recorded|refused, status, code?,
    message?, messageId?, params? }], recorded, alreadyRecorded, refused }, always 200 once the body is
    valid. Repeating a payment is safe (already_recorded). An invoice approved by an API key is still
    refused. API key with the payments:record scope only, minted with a procurementRole that can edit
    invoices.

    Args:
        body (RecordPaymentsBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordPaymentsResult]
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
    body: RecordPaymentsBatchInput,
) -> Optional[RecordPaymentsResult]:
    """[Buyer] Record payments your ERP or bank feed already made outside Pleaxy - wires, checks, ACH, card
    - so each supplier gets its payment notice, remittance advice and sync event without anyone retyping
    it: { payments: [{ invoiceId, method, paymentDate, reference, note?, ...RecordPayment's currency and
    withholding fields }] }, 1-50 per call. Each payment follows RecordPayment's rules and is answered
    on its own: { results: [{ invoiceId, outcome: recorded|already_recorded|refused, status, code?,
    message?, messageId?, params? }], recorded, alreadyRecorded, refused }, always 200 once the body is
    valid. Repeating a payment is safe (already_recorded). An invoice approved by an API key is still
    refused. API key with the payments:record scope only, minted with a procurementRole that can edit
    invoices.

    Args:
        body (RecordPaymentsBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordPaymentsResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RecordPaymentsBatchInput,
) -> Response[RecordPaymentsResult]:
    """[Buyer] Record payments your ERP or bank feed already made outside Pleaxy - wires, checks, ACH, card
    - so each supplier gets its payment notice, remittance advice and sync event without anyone retyping
    it: { payments: [{ invoiceId, method, paymentDate, reference, note?, ...RecordPayment's currency and
    withholding fields }] }, 1-50 per call. Each payment follows RecordPayment's rules and is answered
    on its own: { results: [{ invoiceId, outcome: recorded|already_recorded|refused, status, code?,
    message?, messageId?, params? }], recorded, alreadyRecorded, refused }, always 200 once the body is
    valid. Repeating a payment is safe (already_recorded). An invoice approved by an API key is still
    refused. API key with the payments:record scope only, minted with a procurementRole that can edit
    invoices.

    Args:
        body (RecordPaymentsBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecordPaymentsResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RecordPaymentsBatchInput,
) -> Optional[RecordPaymentsResult]:
    """[Buyer] Record payments your ERP or bank feed already made outside Pleaxy - wires, checks, ACH, card
    - so each supplier gets its payment notice, remittance advice and sync event without anyone retyping
    it: { payments: [{ invoiceId, method, paymentDate, reference, note?, ...RecordPayment's currency and
    withholding fields }] }, 1-50 per call. Each payment follows RecordPayment's rules and is answered
    on its own: { results: [{ invoiceId, outcome: recorded|already_recorded|refused, status, code?,
    message?, messageId?, params? }], recorded, alreadyRecorded, refused }, always 200 once the body is
    valid. Repeating a payment is safe (already_recorded). An invoice approved by an API key is still
    refused. API key with the payments:record scope only, minted with a procurementRole that can edit
    invoices.

    Args:
        body (RecordPaymentsBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecordPaymentsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
