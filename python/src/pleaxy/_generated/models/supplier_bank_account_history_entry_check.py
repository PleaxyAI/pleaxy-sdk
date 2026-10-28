from typing import Literal, Set, cast

SupplierBankAccountHistoryEntryCheck = Literal[
    "bank_letter", "call", "email", "none", "other", "supplier_portal"
]

SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_CHECK_VALUES: Set[
    SupplierBankAccountHistoryEntryCheck
] = {
    "bank_letter",
    "call",
    "email",
    "none",
    "other",
    "supplier_portal",
}


def check_supplier_bank_account_history_entry_check(
    value: str,
) -> SupplierBankAccountHistoryEntryCheck:
    if value in SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_CHECK_VALUES:
        return cast(SupplierBankAccountHistoryEntryCheck, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_CHECK_VALUES!r}"
    )
