from typing import Literal, Set, cast

StartStripePaymentResultState = Literal["checkout_open", "processing", "succeeded"]

START_STRIPE_PAYMENT_RESULT_STATE_VALUES: Set[StartStripePaymentResultState] = {
    "checkout_open",
    "processing",
    "succeeded",
}


def check_start_stripe_payment_result_state(
    value: str,
) -> StartStripePaymentResultState:
    if value in START_STRIPE_PAYMENT_RESULT_STATE_VALUES:
        return cast(StartStripePaymentResultState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {START_STRIPE_PAYMENT_RESULT_STATE_VALUES!r}"
    )
