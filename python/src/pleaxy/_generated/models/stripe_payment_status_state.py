from typing import Literal, Set, cast

StripePaymentStatusState = Literal["checkout_open", "processing", "succeeded"]

STRIPE_PAYMENT_STATUS_STATE_VALUES: Set[StripePaymentStatusState] = {
    "checkout_open",
    "processing",
    "succeeded",
}


def check_stripe_payment_status_state(value: str) -> StripePaymentStatusState:
    if value in STRIPE_PAYMENT_STATUS_STATE_VALUES:
        return cast(StripePaymentStatusState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRIPE_PAYMENT_STATUS_STATE_VALUES!r}"
    )
