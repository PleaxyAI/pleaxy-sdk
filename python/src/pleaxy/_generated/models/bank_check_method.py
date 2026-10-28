from typing import Literal, Set, cast

BankCheckMethod = Literal[
    "bank_letter", "call", "email", "none", "other", "supplier_portal"
]

BANK_CHECK_METHOD_VALUES: Set[BankCheckMethod] = {
    "bank_letter",
    "call",
    "email",
    "none",
    "other",
    "supplier_portal",
}


def check_bank_check_method(value: str) -> BankCheckMethod:
    if value in BANK_CHECK_METHOD_VALUES:
        return cast(BankCheckMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_CHECK_METHOD_VALUES!r}"
    )
