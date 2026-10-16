from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNotePoEffectType1Kind = Literal["none"]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    ListInvoicesItemSupplierCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_list_invoices_item_supplier_credit_note_po_effect_type_1_kind(
    value: str,
) -> ListInvoicesItemSupplierCreditNotePoEffectType1Kind:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(ListInvoicesItemSupplierCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
