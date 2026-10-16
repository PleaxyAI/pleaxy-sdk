from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteDocumentType = Literal[
    "credit_note", "debit_note", "invoice"
]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteDocumentType
] = {
    "credit_note",
    "debit_note",
    "invoice",
}


def check_list_invoices_item_supplier_credit_note_document_type(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteDocumentType:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
