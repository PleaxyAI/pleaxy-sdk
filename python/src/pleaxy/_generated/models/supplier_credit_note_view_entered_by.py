from typing import Literal, Set, cast

SupplierCreditNoteViewEnteredBy = Literal["buyer", "supplier"]

SUPPLIER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES: Set[SupplierCreditNoteViewEnteredBy] = {
    "buyer",
    "supplier",
}


def check_supplier_credit_note_view_entered_by(
    value: str,
) -> SupplierCreditNoteViewEnteredBy:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES:
        return cast(SupplierCreditNoteViewEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES!r}"
    )
