from typing import Literal, Set, cast

RecordPaymentResultSubmittedFormat = Literal["cxml", "json", "ubl"]

RECORD_PAYMENT_RESULT_SUBMITTED_FORMAT_VALUES: Set[
    RecordPaymentResultSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_record_payment_result_submitted_format(
    value: str,
) -> RecordPaymentResultSubmittedFormat:
    if value in RECORD_PAYMENT_RESULT_SUBMITTED_FORMAT_VALUES:
        return cast(RecordPaymentResultSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_SUBMITTED_FORMAT_VALUES!r}"
    )
