from typing import Literal, Set, cast

BuyerCreditNoteViewPoEffectType1Kind = Literal["none"]

BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    BuyerCreditNoteViewPoEffectType1Kind
] = {
    "none",
}


def check_buyer_credit_note_view_po_effect_type_1_kind(
    value: str,
) -> BuyerCreditNoteViewPoEffectType1Kind:
    if value in BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(BuyerCreditNoteViewPoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
