from typing import Literal, Set, cast

BuyerCreditNoteViewStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

BUYER_CREDIT_NOTE_VIEW_STATUS_VALUES: Set[BuyerCreditNoteViewStatus] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_buyer_credit_note_view_status(value: str) -> BuyerCreditNoteViewStatus:
    if value in BUYER_CREDIT_NOTE_VIEW_STATUS_VALUES:
        return cast(BuyerCreditNoteViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_STATUS_VALUES!r}"
    )
