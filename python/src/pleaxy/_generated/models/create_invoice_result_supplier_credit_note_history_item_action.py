from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteHistoryItemAction = Literal[
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteHistoryItemAction
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


def check_create_invoice_result_supplier_credit_note_history_item_action(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteHistoryItemAction:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteHistoryItemAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_HISTORY_ITEM_ACTION_VALUES!r}"
    )
