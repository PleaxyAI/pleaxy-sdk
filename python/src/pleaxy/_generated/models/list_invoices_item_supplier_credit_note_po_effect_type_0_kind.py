from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNotePoEffectType0Kind = Literal["release"]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES: Set[
    ListInvoicesItemSupplierCreditNotePoEffectType0Kind
] = {
    "release",
}


def check_list_invoices_item_supplier_credit_note_po_effect_type_0_kind(
    value: str,
) -> ListInvoicesItemSupplierCreditNotePoEffectType0Kind:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES:
        return cast(ListInvoicesItemSupplierCreditNotePoEffectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES!r}"
    )
