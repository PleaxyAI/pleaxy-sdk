from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_STATUS_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_list_invoices_item_buyer_credit_note_status(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteStatus:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_STATUS_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
