from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceDocumentType = Literal["debit_note"]

LIST_INVOICES_ITEM_BUYER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    ListInvoicesItemBuyerInvoiceDocumentType
] = {
    "debit_note",
}


def check_list_invoices_item_buyer_invoice_document_type(
    value: str,
) -> ListInvoicesItemBuyerInvoiceDocumentType:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
