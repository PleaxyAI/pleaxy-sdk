from typing import Literal, Set, cast

BuyerCreditNoteViewReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

BUYER_CREDIT_NOTE_VIEW_REASON_VALUES: Set[BuyerCreditNoteViewReason] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_buyer_credit_note_view_reason(value: str) -> BuyerCreditNoteViewReason:
    if value in BUYER_CREDIT_NOTE_VIEW_REASON_VALUES:
        return cast(BuyerCreditNoteViewReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_REASON_VALUES!r}"
    )
