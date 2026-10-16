from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteSubmittedFormat = Literal["cxml", "json", "ubl"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_get_invoice_result_supplier_credit_note_submitted_format(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteSubmittedFormat:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
