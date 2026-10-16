from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteSource = Literal["cloud_sync", "feed"]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_list_invoices_item_supplier_credit_note_source(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteSource:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
