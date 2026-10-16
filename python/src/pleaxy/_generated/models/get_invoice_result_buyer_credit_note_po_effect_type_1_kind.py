from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNotePoEffectType1Kind = Literal["none"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    GetInvoiceResultBuyerCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_get_invoice_result_buyer_credit_note_po_effect_type_1_kind(
    value: str,
) -> GetInvoiceResultBuyerCreditNotePoEffectType1Kind:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(GetInvoiceResultBuyerCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
