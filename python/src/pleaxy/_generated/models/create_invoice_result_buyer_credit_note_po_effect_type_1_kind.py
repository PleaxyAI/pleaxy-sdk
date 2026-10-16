from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNotePoEffectType1Kind = Literal["none"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    CreateInvoiceResultBuyerCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_create_invoice_result_buyer_credit_note_po_effect_type_1_kind(
    value: str,
) -> CreateInvoiceResultBuyerCreditNotePoEffectType1Kind:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
