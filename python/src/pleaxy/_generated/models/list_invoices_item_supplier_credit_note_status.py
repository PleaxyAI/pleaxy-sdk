from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_STATUS_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_list_invoices_item_supplier_credit_note_status(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteStatus:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_STATUS_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
