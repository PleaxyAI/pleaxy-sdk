from typing import Literal, Set, cast

BuyerCreditNoteViewPoEffectType1Why = Literal["no_po", "not_a_correction", "po_closed"]

BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    BuyerCreditNoteViewPoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_buyer_credit_note_view_po_effect_type_1_why(
    value: str,
) -> BuyerCreditNoteViewPoEffectType1Why:
    if value in BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(BuyerCreditNoteViewPoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
