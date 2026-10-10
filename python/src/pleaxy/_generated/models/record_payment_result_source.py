from typing import Literal, Set, cast

RecordPaymentResultSource = Literal["direct", "feed", "manual", "po-flip"]

RECORD_PAYMENT_RESULT_SOURCE_VALUES: Set[RecordPaymentResultSource] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_record_payment_result_source(value: str) -> RecordPaymentResultSource:
    if value in RECORD_PAYMENT_RESULT_SOURCE_VALUES:
        return cast(RecordPaymentResultSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_SOURCE_VALUES!r}"
    )
