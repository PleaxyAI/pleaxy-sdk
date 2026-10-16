from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNotePoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    ListInvoicesItemSupplierCreditNotePoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_list_invoices_item_supplier_credit_note_po_effect_type_1_why(
    value: str,
) -> ListInvoicesItemSupplierCreditNotePoEffectType1Why:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(ListInvoicesItemSupplierCreditNotePoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
