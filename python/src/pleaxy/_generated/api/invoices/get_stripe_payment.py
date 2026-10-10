from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stripe_payment_status import StripePaymentStatus
from ...types import Response


def _get_kwargs(
    invoice_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/invoices/{invoice_id}/stripe-payment".format(
            invoice_id=invoice_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StripePaymentStatus]:
    if response.status_code == 200:
        response_200 = StripePaymentStatus.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StripePaymentStatus]:
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
) -> Response[StripePaymentStatus]:
    """[Buyer] Whether this invoice can be paid through Pleaxy with Stripe: { available, reason?, state?,
    paymentMethodType?, quote? }. `quote` is { amount, fee, total, currency } in dollars: the buyer
    covers Stripe's bank-transfer fee (0.8%, capped at $5) so the supplier receives the full invoice
    amount. `reason` explains why not (not_configured, not_approved, payment_locked,
    supplier_not_on_pleaxy, supplier_not_connected, unsupported_currency, amount_too_small). `state` is
    the current Stripe payment: checkout_open, processing (a bank transfer clearing) or succeeded.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StripePaymentStatus]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[StripePaymentStatus]:
    """[Buyer] Whether this invoice can be paid through Pleaxy with Stripe: { available, reason?, state?,
    paymentMethodType?, quote? }. `quote` is { amount, fee, total, currency } in dollars: the buyer
    covers Stripe's bank-transfer fee (0.8%, capped at $5) so the supplier receives the full invoice
    amount. `reason` explains why not (not_configured, not_approved, payment_locked,
    supplier_not_on_pleaxy, supplier_not_connected, unsupported_currency, amount_too_small). `state` is
    the current Stripe payment: checkout_open, processing (a bank transfer clearing) or succeeded.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StripePaymentStatus
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[StripePaymentStatus]:
    """[Buyer] Whether this invoice can be paid through Pleaxy with Stripe: { available, reason?, state?,
    paymentMethodType?, quote? }. `quote` is { amount, fee, total, currency } in dollars: the buyer
    covers Stripe's bank-transfer fee (0.8%, capped at $5) so the supplier receives the full invoice
    amount. `reason` explains why not (not_configured, not_approved, payment_locked,
    supplier_not_on_pleaxy, supplier_not_connected, unsupported_currency, amount_too_small). `state` is
    the current Stripe payment: checkout_open, processing (a bank transfer clearing) or succeeded.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StripePaymentStatus]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[StripePaymentStatus]:
    """[Buyer] Whether this invoice can be paid through Pleaxy with Stripe: { available, reason?, state?,
    paymentMethodType?, quote? }. `quote` is { amount, fee, total, currency } in dollars: the buyer
    covers Stripe's bank-transfer fee (0.8%, capped at $5) so the supplier receives the full invoice
    amount. `reason` explains why not (not_configured, not_approved, payment_locked,
    supplier_not_on_pleaxy, supplier_not_connected, unsupported_currency, amount_too_small). `state` is
    the current Stripe payment: checkout_open, processing (a bank transfer clearing) or succeeded.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StripePaymentStatus
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
