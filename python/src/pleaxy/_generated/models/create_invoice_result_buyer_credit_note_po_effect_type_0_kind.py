from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNotePoEffectType0Kind = Literal["release"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES: Set[
    CreateInvoiceResultBuyerCreditNotePoEffectType0Kind
] = {
    "release",
}


def check_create_invoice_result_buyer_credit_note_po_effect_type_0_kind(
    value: str,
) -> CreateInvoiceResultBuyerCreditNotePoEffectType0Kind:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNotePoEffectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES!r}"
    )
