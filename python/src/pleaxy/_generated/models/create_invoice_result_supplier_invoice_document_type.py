from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceDocumentType = Literal["debit_note", "invoice"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_create_invoice_result_supplier_invoice_document_type(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceDocumentType:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
