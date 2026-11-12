from typing import Literal, Set, cast

CreateCreditNoteInputReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

CREATE_CREDIT_NOTE_INPUT_REASON_VALUES: Set[CreateCreditNoteInputReason] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_create_credit_note_input_reason(value: str) -> CreateCreditNoteInputReason:
    if value in CREATE_CREDIT_NOTE_INPUT_REASON_VALUES:
        return cast(CreateCreditNoteInputReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CREDIT_NOTE_INPUT_REASON_VALUES!r}"
    )
