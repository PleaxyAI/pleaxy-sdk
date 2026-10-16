from typing import Literal, Set, cast

SupplierCreditNoteViewPoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    SupplierCreditNoteViewPoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_supplier_credit_note_view_po_effect_type_1_why(
    value: str,
) -> SupplierCreditNoteViewPoEffectType1Why:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(SupplierCreditNoteViewPoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
