from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNotePoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    GetInvoiceResultSupplierCreditNotePoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_get_invoice_result_supplier_credit_note_po_effect_type_1_why(
    value: str,
) -> GetInvoiceResultSupplierCreditNotePoEffectType1Why:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(GetInvoiceResultSupplierCreditNotePoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
