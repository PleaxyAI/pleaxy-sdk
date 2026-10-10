from typing import Literal, Set, cast

RemittanceInstructionsInputMethod = Literal[
    "ach", "bank_transfer", "check", "other", "wire"
]

REMITTANCE_INSTRUCTIONS_INPUT_METHOD_VALUES: Set[RemittanceInstructionsInputMethod] = {
    "ach",
    "bank_transfer",
    "check",
    "other",
    "wire",
}


def check_remittance_instructions_input_method(
    value: str,
) -> RemittanceInstructionsInputMethod:
    if value in REMITTANCE_INSTRUCTIONS_INPUT_METHOD_VALUES:
        return cast(RemittanceInstructionsInputMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_INSTRUCTIONS_INPUT_METHOD_VALUES!r}"
    )
