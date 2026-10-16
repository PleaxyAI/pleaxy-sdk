from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteDocumentType = Literal["credit_note"]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteDocumentType
] = {
    "credit_note",
}


def check_create_invoice_result_supplier_credit_note_document_type(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteDocumentType:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
