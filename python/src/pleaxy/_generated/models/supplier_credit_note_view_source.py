from typing import Literal, Set, cast

SupplierCreditNoteViewSource = Literal["cloud_sync", "feed"]

SUPPLIER_CREDIT_NOTE_VIEW_SOURCE_VALUES: Set[SupplierCreditNoteViewSource] = {
    "cloud_sync",
    "feed",
}


def check_supplier_credit_note_view_source(value: str) -> SupplierCreditNoteViewSource:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_SOURCE_VALUES:
        return cast(SupplierCreditNoteViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_SOURCE_VALUES!r}"
    )
