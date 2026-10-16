from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteHistoryItemAction = Literal[
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteHistoryItemAction
] = {
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
}


def check_list_invoices_item_supplier_credit_note_history_item_action(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteHistoryItemAction:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteHistoryItemAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES!r}"
    )
