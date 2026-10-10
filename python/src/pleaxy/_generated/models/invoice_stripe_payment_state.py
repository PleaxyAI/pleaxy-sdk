from typing import Literal, Set, cast

InvoiceStripePaymentState = Literal["checkout_open", "processing", "succeeded"]

INVOICE_STRIPE_PAYMENT_STATE_VALUES: Set[InvoiceStripePaymentState] = {
    "checkout_open",
    "processing",
    "succeeded",
}


def check_invoice_stripe_payment_state(value: str) -> InvoiceStripePaymentState:
    if value in INVOICE_STRIPE_PAYMENT_STATE_VALUES:
        return cast(InvoiceStripePaymentState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STRIPE_PAYMENT_STATE_VALUES!r}"
    )
