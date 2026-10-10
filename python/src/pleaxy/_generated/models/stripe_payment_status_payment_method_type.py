from typing import Literal, Set, cast

StripePaymentStatusPaymentMethodType = Literal["card", "us_bank_account"]

STRIPE_PAYMENT_STATUS_PAYMENT_METHOD_TYPE_VALUES: Set[
    StripePaymentStatusPaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_stripe_payment_status_payment_method_type(
    value: str,
) -> StripePaymentStatusPaymentMethodType:
    if value in STRIPE_PAYMENT_STATUS_PAYMENT_METHOD_TYPE_VALUES:
        return cast(StripePaymentStatusPaymentMethodType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRIPE_PAYMENT_STATUS_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
