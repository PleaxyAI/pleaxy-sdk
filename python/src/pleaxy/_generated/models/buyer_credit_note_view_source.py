from typing import Literal, Set, cast

BuyerCreditNoteViewSource = Literal["cloud_sync", "feed"]

BUYER_CREDIT_NOTE_VIEW_SOURCE_VALUES: Set[BuyerCreditNoteViewSource] = {
    "cloud_sync",
    "feed",
}


def check_buyer_credit_note_view_source(value: str) -> BuyerCreditNoteViewSource:
    if value in BUYER_CREDIT_NOTE_VIEW_SOURCE_VALUES:
        return cast(BuyerCreditNoteViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_SOURCE_VALUES!r}"
    )
