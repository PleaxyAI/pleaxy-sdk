from typing import Literal, Set, cast

SupplierCreditNoteViewPoEffectType1Kind = Literal["none"]

SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    SupplierCreditNoteViewPoEffectType1Kind
] = {
    "none",
}


def check_supplier_credit_note_view_po_effect_type_1_kind(
    value: str,
) -> SupplierCreditNoteViewPoEffectType1Kind:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(SupplierCreditNoteViewPoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
