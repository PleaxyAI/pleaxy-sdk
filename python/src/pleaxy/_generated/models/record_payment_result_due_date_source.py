from typing import Literal, Set, cast

RecordPaymentResultDueDateSource = Literal["default", "stated"]

RECORD_PAYMENT_RESULT_DUE_DATE_SOURCE_VALUES: Set[RecordPaymentResultDueDateSource] = {
    "default",
    "stated",
}


def check_record_payment_result_due_date_source(
    value: str,
) -> RecordPaymentResultDueDateSource:
    if value in RECORD_PAYMENT_RESULT_DUE_DATE_SOURCE_VALUES:
        return cast(RecordPaymentResultDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_DUE_DATE_SOURCE_VALUES!r}"
    )
