from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNotePoEffectType1Why = Literal[
    "no_po", "not_a_correction", "po_closed"
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES: Set[
    CreateInvoiceResultSupplierCreditNotePoEffectType1Why
] = {
    "no_po",
    "not_a_correction",
    "po_closed",
}


def check_create_invoice_result_supplier_credit_note_po_effect_type_1_why(
    value: str,
) -> CreateInvoiceResultSupplierCreditNotePoEffectType1Why:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNotePoEffectType1Why, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_WHY_VALUES!r}"
    )
