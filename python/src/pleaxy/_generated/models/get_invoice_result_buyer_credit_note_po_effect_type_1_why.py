from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNotePoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    GetInvoiceResultBuyerCreditNotePoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_get_invoice_result_buyer_credit_note_po_effect_type_1_why(
    value: str,
) -> GetInvoiceResultBuyerCreditNotePoEffectType1Why:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(GetInvoiceResultBuyerCreditNotePoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
