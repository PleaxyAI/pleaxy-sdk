from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteEnteredBy = Literal["buyer", "supplier"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_get_invoice_result_supplier_credit_note_entered_by(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteEnteredBy:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES!r}"
    )
