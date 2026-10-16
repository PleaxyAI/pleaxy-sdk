from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_REASON_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_list_invoices_item_supplier_credit_note_reason(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteReason:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_REASON_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_REASON_VALUES!r}"
    )
