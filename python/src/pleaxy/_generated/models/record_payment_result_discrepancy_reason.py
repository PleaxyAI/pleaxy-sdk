from typing import Literal, Set, cast

RecordPaymentResultDiscrepancyReason = Literal[
    "amount", "controls", "currency", "no_po_variance"
]

RECORD_PAYMENT_RESULT_DISCREPANCY_REASON_VALUES: Set[
    RecordPaymentResultDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
    "no_po_variance",
}


def check_record_payment_result_discrepancy_reason(
    value: str,
) -> RecordPaymentResultDiscrepancyReason:
    if value in RECORD_PAYMENT_RESULT_DISCREPANCY_REASON_VALUES:
        return cast(RecordPaymentResultDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_DISCREPANCY_REASON_VALUES!r}"
    )
