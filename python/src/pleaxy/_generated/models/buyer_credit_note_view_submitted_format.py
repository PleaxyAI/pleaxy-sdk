from typing import Literal, Set, cast

BuyerCreditNoteViewSubmittedFormat = Literal["cxml", "json", "ubl"]

BUYER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES: Set[
    BuyerCreditNoteViewSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_buyer_credit_note_view_submitted_format(
    value: str,
) -> BuyerCreditNoteViewSubmittedFormat:
    if value in BUYER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES:
        return cast(BuyerCreditNoteViewSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_SUBMITTED_FORMAT_VALUES!r}"
    )
