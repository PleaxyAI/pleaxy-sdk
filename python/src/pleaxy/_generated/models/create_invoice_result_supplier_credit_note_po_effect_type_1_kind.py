from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNotePoEffectType1Kind = Literal["none"]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    CreateInvoiceResultSupplierCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_create_invoice_result_supplier_credit_note_po_effect_type_1_kind(
    value: str,
) -> CreateInvoiceResultSupplierCreditNotePoEffectType1Kind:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
