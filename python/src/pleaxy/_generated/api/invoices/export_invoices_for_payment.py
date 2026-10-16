from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.payment_export_input import PaymentExportInput
from ...types import File, Response


def _get_kwargs(
    *,
    body: PaymentExportInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/payment-export",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[File]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentExportInput,
) -> Response[File]:
    """[Buyer] Export approved, unpaid invoices as CSV for your own payment run, due date first, up to
    1,000. Send { invoiceIds: [...] } to export only those (a row's Export for payment); without it,
    every eligible invoice. A replaced invoice its credit notes don't cover in full is left out of a
    full export, and is 409 REPLACED_UNCREDITED when named until you send confirmReplaced: true (credit
    and rebill). Each exported invoice is locked until its payment is recorded or the export is
    withdrawn. Headers: X-Pleaxy-Export-Id, X-Pleaxy-Export-Count, X-Pleaxy-Export-Truncated. 422
    NOTHING_TO_EXPORT when none are eligible. No bank details. Human session only.

    Args:
        body (PaymentExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
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
    body: PaymentExportInput,
) -> Optional[File]:
    """[Buyer] Export approved, unpaid invoices as CSV for your own payment run, due date first, up to
    1,000. Send { invoiceIds: [...] } to export only those (a row's Export for payment); without it,
    every eligible invoice. A replaced invoice its credit notes don't cover in full is left out of a
    full export, and is 409 REPLACED_UNCREDITED when named until you send confirmReplaced: true (credit
    and rebill). Each exported invoice is locked until its payment is recorded or the export is
    withdrawn. Headers: X-Pleaxy-Export-Id, X-Pleaxy-Export-Count, X-Pleaxy-Export-Truncated. 422
    NOTHING_TO_EXPORT when none are eligible. No bank details. Human session only.

    Args:
        body (PaymentExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentExportInput,
) -> Response[File]:
    """[Buyer] Export approved, unpaid invoices as CSV for your own payment run, due date first, up to
    1,000. Send { invoiceIds: [...] } to export only those (a row's Export for payment); without it,
    every eligible invoice. A replaced invoice its credit notes don't cover in full is left out of a
    full export, and is 409 REPLACED_UNCREDITED when named until you send confirmReplaced: true (credit
    and rebill). Each exported invoice is locked until its payment is recorded or the export is
    withdrawn. Headers: X-Pleaxy-Export-Id, X-Pleaxy-Export-Count, X-Pleaxy-Export-Truncated. 422
    NOTHING_TO_EXPORT when none are eligible. No bank details. Human session only.

    Args:
        body (PaymentExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PaymentExportInput,
) -> Optional[File]:
    """[Buyer] Export approved, unpaid invoices as CSV for your own payment run, due date first, up to
    1,000. Send { invoiceIds: [...] } to export only those (a row's Export for payment); without it,
    every eligible invoice. A replaced invoice its credit notes don't cover in full is left out of a
    full export, and is 409 REPLACED_UNCREDITED when named until you send confirmReplaced: true (credit
    and rebill). Each exported invoice is locked until its payment is recorded or the export is
    withdrawn. Headers: X-Pleaxy-Export-Id, X-Pleaxy-Export-Count, X-Pleaxy-Export-Truncated. 422
    NOTHING_TO_EXPORT when none are eligible. No bank details. Human session only.

    Args:
        body (PaymentExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
