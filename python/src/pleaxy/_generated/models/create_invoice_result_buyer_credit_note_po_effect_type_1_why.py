from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNotePoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    CreateInvoiceResultBuyerCreditNotePoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_create_invoice_result_buyer_credit_note_po_effect_type_1_why(
    value: str,
) -> CreateInvoiceResultBuyerCreditNotePoEffectType1Why:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNotePoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
