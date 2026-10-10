from typing import Literal, Set, cast

RecordPaymentInputMethod = Literal["ach", "card", "check", "other", "wire"]

RECORD_PAYMENT_INPUT_METHOD_VALUES: Set[RecordPaymentInputMethod] = {
    "ach",
    "card",
    "check",
    "other",
    "wire",
}


def check_record_payment_input_method(value: str) -> RecordPaymentInputMethod:
    if value in RECORD_PAYMENT_INPUT_METHOD_VALUES:
        return cast(RecordPaymentInputMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_INPUT_METHOD_VALUES!r}"
    )
