from typing import Literal, Set, cast

SupplierCreditNoteViewPoEffectType0Kind = Literal["release"]

SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES: Set[
    SupplierCreditNoteViewPoEffectType0Kind
] = {
    "release",
}


def check_supplier_credit_note_view_po_effect_type_0_kind(
    value: str,
) -> SupplierCreditNoteViewPoEffectType0Kind:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES:
        return cast(SupplierCreditNoteViewPoEffectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_0_KIND_VALUES!r}"
    )
