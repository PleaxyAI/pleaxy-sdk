from typing import Literal, Set, cast

SupplierCreditNoteViewStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

SUPPLIER_CREDIT_NOTE_VIEW_STATUS_VALUES: Set[SupplierCreditNoteViewStatus] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_supplier_credit_note_view_status(value: str) -> SupplierCreditNoteViewStatus:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_STATUS_VALUES:
        return cast(SupplierCreditNoteViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_STATUS_VALUES!r}"
    )
