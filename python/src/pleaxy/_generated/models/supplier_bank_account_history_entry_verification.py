from typing import Literal, Set, cast

SupplierBankAccountHistoryEntryVerification = Literal[
    "buyer_approved", "paid_before", "supplier_confirmed"
]

SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_VERIFICATION_VALUES: Set[
    SupplierBankAccountHistoryEntryVerification
] = {
    "buyer_approved",
    "paid_before",
    "supplier_confirmed",
}


def check_supplier_bank_account_history_entry_verification(
    value: str,
) -> SupplierBankAccountHistoryEntryVerification:
    if value in SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_VERIFICATION_VALUES:
        return cast(SupplierBankAccountHistoryEntryVerification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_VERIFICATION_VALUES!r}"
    )
