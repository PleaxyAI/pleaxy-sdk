from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNotePoEffectType1Kind = Literal["none"]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    ListInvoicesItemBuyerCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_list_invoices_item_buyer_credit_note_po_effect_type_1_kind(
    value: str,
) -> ListInvoicesItemBuyerCreditNotePoEffectType1Kind:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(ListInvoicesItemBuyerCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
