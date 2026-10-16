from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteDocumentType = Literal[
    "credit_note", "debit_note", "invoice"
]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteDocumentType
] = {
    "credit_note",
    "debit_note",
    "invoice",
}


def check_list_invoices_item_buyer_credit_note_document_type(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteDocumentType:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
