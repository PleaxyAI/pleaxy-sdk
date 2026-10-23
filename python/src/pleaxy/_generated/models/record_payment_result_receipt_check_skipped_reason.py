from typing import Literal, Set, cast

RecordPaymentResultReceiptCheckSkippedReason = Literal["small_invoice"]

RECORD_PAYMENT_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    RecordPaymentResultReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_record_payment_result_receipt_check_skipped_reason(
    value: str,
) -> RecordPaymentResultReceiptCheckSkippedReason:
    if value in RECORD_PAYMENT_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES:
        return cast(RecordPaymentResultReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
