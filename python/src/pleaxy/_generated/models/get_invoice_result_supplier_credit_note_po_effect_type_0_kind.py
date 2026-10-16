from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNotePoEffectType0Kind = Literal["release"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES: Set[
    GetInvoiceResultSupplierCreditNotePoEffectType0Kind
] = {
    "release",
}


def check_get_invoice_result_supplier_credit_note_po_effect_type_0_kind(
    value: str,
) -> GetInvoiceResultSupplierCreditNotePoEffectType0Kind:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES:
        return cast(GetInvoiceResultSupplierCreditNotePoEffectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_PO_EFFECT_TYPE_0_KIND_VALUES!r}"
    )
