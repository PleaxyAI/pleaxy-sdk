from typing import Literal, Set, cast

RecordPaymentResultMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

RECORD_PAYMENT_RESULT_MATCH_STATUS_VALUES: Set[RecordPaymentResultMatchStatus] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_record_payment_result_match_status(
    value: str,
) -> RecordPaymentResultMatchStatus:
    if value in RECORD_PAYMENT_RESULT_MATCH_STATUS_VALUES:
        return cast(RecordPaymentResultMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_MATCH_STATUS_VALUES!r}"
    )
