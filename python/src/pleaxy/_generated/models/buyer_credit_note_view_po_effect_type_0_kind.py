from typing import Literal, Set, cast

BuyerCreditNoteViewPoEffectType0Kind = Literal["release"]

BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES: Set[
    BuyerCreditNoteViewPoEffectType0Kind
] = {
    "release",
}


def check_buyer_credit_note_view_po_effect_type_0_kind(
    value: str,
) -> BuyerCreditNoteViewPoEffectType0Kind:
    if value in BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES:
        return cast(BuyerCreditNoteViewPoEffectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES!r}"
    )
