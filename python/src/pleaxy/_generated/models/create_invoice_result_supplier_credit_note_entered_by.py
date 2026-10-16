from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteEnteredBy = Literal["buyer", "supplier"]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_create_invoice_result_supplier_credit_note_entered_by(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteEnteredBy:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_ENTERED_BY_VALUES!r}"
    )
