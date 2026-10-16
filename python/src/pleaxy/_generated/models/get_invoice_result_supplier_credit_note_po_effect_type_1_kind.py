from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNotePoEffectType1Kind = Literal["none"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES: Set[
    GetInvoiceResultSupplierCreditNotePoEffectType1Kind
] = {
    "none",
}


def check_get_invoice_result_supplier_credit_note_po_effect_type_1_kind(
    value: str,
) -> GetInvoiceResultSupplierCreditNotePoEffectType1Kind:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES:
        return cast(GetInvoiceResultSupplierCreditNotePoEffectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_1_KIND_VALUES!r}"
    )
