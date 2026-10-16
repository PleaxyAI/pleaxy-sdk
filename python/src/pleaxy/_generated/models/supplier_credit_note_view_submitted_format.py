from typing import Literal, Set, cast

SupplierCreditNoteViewSubmittedFormat = Literal["cxml", "json", "ubl"]

SUPPLIER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES: Set[
    SupplierCreditNoteViewSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_supplier_credit_note_view_submitted_format(
    value: str,
) -> SupplierCreditNoteViewSubmittedFormat:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES:
        return cast(SupplierCreditNoteViewSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES!r}"
    )
