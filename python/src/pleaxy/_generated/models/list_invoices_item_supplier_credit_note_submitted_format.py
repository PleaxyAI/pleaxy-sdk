from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteSubmittedFormat = Literal["cxml", "json", "ubl"]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_list_invoices_item_supplier_credit_note_submitted_format(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteSubmittedFormat:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
