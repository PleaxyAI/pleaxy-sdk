from typing import Literal, Set, cast

RemittanceInstructionsMethod = Literal["ach", "bank_transfer", "check", "other", "wire"]

REMITTANCE_INSTRUCTIONS_METHOD_VALUES: Set[RemittanceInstructionsMethod] = {
    "ach",
    "bank_transfer",
    "check",
    "other",
    "wire",
}


def check_remittance_instructions_method(value: str) -> RemittanceInstructionsMethod:
    if value in REMITTANCE_INSTRUCTIONS_METHOD_VALUES:
        return cast(RemittanceInstructionsMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_INSTRUCTIONS_METHOD_VALUES!r}"
    )
