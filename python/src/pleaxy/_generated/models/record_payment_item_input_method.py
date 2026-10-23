from typing import Literal, Set, cast

RecordPaymentItemInputMethod = Literal["ach", "card", "check", "other", "wire"]

RECORD_PAYMENT_ITEM_INPUT_METHOD_VALUES: Set[RecordPaymentItemInputMethod] = {
    "ach",
    "card",
    "check",
    "other",
    "wire",
}


def check_record_payment_item_input_method(value: str) -> RecordPaymentItemInputMethod:
    if value in RECORD_PAYMENT_ITEM_INPUT_METHOD_VALUES:
        return cast(RecordPaymentItemInputMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_ITEM_INPUT_METHOD_VALUES!r}"
    )
