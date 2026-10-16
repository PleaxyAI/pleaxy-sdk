from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteHistoryItemAction = Literal[
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteHistoryItemAction
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


def check_get_invoice_result_supplier_credit_note_history_item_action(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteHistoryItemAction:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteHistoryItemAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES!r}"
    )
