from typing import Literal, Set, cast

SupplierCreditNoteViewHistoryItemAction = Literal[
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
]

SUPPLIER_CREDIT_NOTE_VIEW_HISTORY_ITEM_ACTION_VALUES: Set[
    SupplierCreditNoteViewHistoryItemAction
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


def check_supplier_credit_note_view_history_item_action(
    value: str,
) -> SupplierCreditNoteViewHistoryItemAction:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_HISTORY_ITEM_ACTION_VALUES:
        return cast(SupplierCreditNoteViewHistoryItemAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_HISTORY_ITEM_ACTION_VALUES!r}"
    )
