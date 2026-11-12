from typing import Literal, Set, cast

BuyerCreditNoteViewEnteredBy = Literal["buyer", "supplier"]

BUYER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES: Set[BuyerCreditNoteViewEnteredBy] = {
    "buyer",
    "supplier",
}


def check_buyer_credit_note_view_entered_by(value: str) -> BuyerCreditNoteViewEnteredBy:
    if value in BUYER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES:
        return cast(BuyerCreditNoteViewEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_ENTERED_BY_VALUES!r}"
    )
