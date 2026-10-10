from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_stripe_payment_result import StartStripePaymentResult
from ...types import Response


def _get_kwargs(
    invoice_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/stripe-payment".format(
            invoice_id=invoice_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StartStripePaymentResult]:
    if response.status_code == 201:
        response_201 = StartStripePaymentResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StartStripePaymentResult]:
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
) -> Response[StartStripePaymentResult]:
    """[Buyer] Pay this approved invoice in full through Pleaxy with Stripe: { url } of a Stripe Checkout
    page (US bank transfer only), on the supplier's own Stripe account. The buyer pays the invoice plus
    Stripe's fee, so the supplier receives the full invoice amount; Pleaxy charges nothing and never
    holds the money. The invoice is locked while Checkout is open (up to an hour) and marked paid when
    Stripe confirms it. Resumes an open Checkout; answers { state } with no url when a payment is
    already processing or done. 422 STRIPE_* when this invoice can't be paid this way. Human session
    only.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartStripePaymentResult]
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
) -> Optional[StartStripePaymentResult]:
    """[Buyer] Pay this approved invoice in full through Pleaxy with Stripe: { url } of a Stripe Checkout
    page (US bank transfer only), on the supplier's own Stripe account. The buyer pays the invoice plus
    Stripe's fee, so the supplier receives the full invoice amount; Pleaxy charges nothing and never
    holds the money. The invoice is locked while Checkout is open (up to an hour) and marked paid when
    Stripe confirms it. Resumes an open Checkout; answers { state } with no url when a payment is
    already processing or done. 422 STRIPE_* when this invoice can't be paid this way. Human session
    only.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartStripePaymentResult
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[StartStripePaymentResult]:
    """[Buyer] Pay this approved invoice in full through Pleaxy with Stripe: { url } of a Stripe Checkout
    page (US bank transfer only), on the supplier's own Stripe account. The buyer pays the invoice plus
    Stripe's fee, so the supplier receives the full invoice amount; Pleaxy charges nothing and never
    holds the money. The invoice is locked while Checkout is open (up to an hour) and marked paid when
    Stripe confirms it. Resumes an open Checkout; answers { state } with no url when a payment is
    already processing or done. 422 STRIPE_* when this invoice can't be paid this way. Human session
    only.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartStripePaymentResult]
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
) -> Optional[StartStripePaymentResult]:
    """[Buyer] Pay this approved invoice in full through Pleaxy with Stripe: { url } of a Stripe Checkout
    page (US bank transfer only), on the supplier's own Stripe account. The buyer pays the invoice plus
    Stripe's fee, so the supplier receives the full invoice amount; Pleaxy charges nothing and never
    holds the money. The invoice is locked while Checkout is open (up to an hour) and marked paid when
    Stripe confirms it. Resumes an open Checkout; answers { state } with no url when a payment is
    already processing or done. 422 STRIPE_* when this invoice can't be paid this way. Human session
    only.

    Args:
        invoice_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartStripePaymentResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
