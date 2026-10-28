from typing import Literal, Set, cast

SupplierBankAccountHistoryEntryEvent = Literal[
    "approved", "change_proposed", "change_rejected", "learned", "seeded"
]

SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_EVENT_VALUES: Set[
    SupplierBankAccountHistoryEntryEvent
] = {
    "approved",
    "change_proposed",
    "change_rejected",
    "learned",
    "seeded",
}


def check_supplier_bank_account_history_entry_event(
    value: str,
) -> SupplierBankAccountHistoryEntryEvent:
    if value in SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_EVENT_VALUES:
        return cast(SupplierBankAccountHistoryEntryEvent, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_HISTORY_ENTRY_EVENT_VALUES!r}"
    )
