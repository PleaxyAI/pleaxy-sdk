from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteDocumentType = Literal["credit_note"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteDocumentType
] = {
    "credit_note",
}


def check_get_invoice_result_supplier_credit_note_document_type(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteDocumentType:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
