from typing import Literal, Set, cast

RecordPaymentResultUnverifiedReason = Literal[
    "no_billing_connection", "no_purchase_order"
]

RECORD_PAYMENT_RESULT_UNVERIFIED_REASON_VALUES: Set[
    RecordPaymentResultUnverifiedReason
] = {
    "no_billing_connection",
    "no_purchase_order",
}


def check_record_payment_result_unverified_reason(
    value: str,
) -> RecordPaymentResultUnverifiedReason:
    if value in RECORD_PAYMENT_RESULT_UNVERIFIED_REASON_VALUES:
        return cast(RecordPaymentResultUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_UNVERIFIED_REASON_VALUES!r}"
    )
