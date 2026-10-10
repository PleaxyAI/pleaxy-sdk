from typing import Literal, Set, cast

RecordPaymentResultEnteredBy = Literal["buyer", "supplier"]

RECORD_PAYMENT_RESULT_ENTERED_BY_VALUES: Set[RecordPaymentResultEnteredBy] = {
    "buyer",
    "supplier",
}


def check_record_payment_result_entered_by(value: str) -> RecordPaymentResultEnteredBy:
    if value in RECORD_PAYMENT_RESULT_ENTERED_BY_VALUES:
        return cast(RecordPaymentResultEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_ENTERED_BY_VALUES!r}"
    )
