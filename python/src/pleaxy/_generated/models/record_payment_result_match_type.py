from typing import Literal, Set, cast

RecordPaymentResultMatchType = Literal["three_way", "two_way", "usage"]

RECORD_PAYMENT_RESULT_MATCH_TYPE_VALUES: Set[RecordPaymentResultMatchType] = {
    "three_way",
    "two_way",
    "usage",
}


def check_record_payment_result_match_type(value: str) -> RecordPaymentResultMatchType:
    if value in RECORD_PAYMENT_RESULT_MATCH_TYPE_VALUES:
        return cast(RecordPaymentResultMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_MATCH_TYPE_VALUES!r}"
    )
