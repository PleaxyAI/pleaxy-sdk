from typing import Literal, Set, cast

StripePaymentStatusReason = Literal[
    "amount_too_small",
    "bank_details_held",
    "not_approved",
    "not_configured",
    "payment_locked",
    "supplier_not_connected",
    "supplier_not_on_pleaxy",
    "unsupported_currency",
]

STRIPE_PAYMENT_STATUS_REASON_VALUES: Set[StripePaymentStatusReason] = {
    "amount_too_small",
    "bank_details_held",
    "not_approved",
    "not_configured",
    "payment_locked",
    "supplier_not_connected",
    "supplier_not_on_pleaxy",
    "unsupported_currency",
}


def check_stripe_payment_status_reason(value: str) -> StripePaymentStatusReason:
    if value in STRIPE_PAYMENT_STATUS_REASON_VALUES:
        return cast(StripePaymentStatusReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRIPE_PAYMENT_STATUS_REASON_VALUES!r}"
    )
