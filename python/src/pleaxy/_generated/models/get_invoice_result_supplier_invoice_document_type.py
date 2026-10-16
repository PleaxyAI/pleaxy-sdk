from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceDocumentType = Literal["debit_note", "invoice"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    GetInvoiceResultSupplierInvoiceDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_get_invoice_result_supplier_invoice_document_type(
    value: str,
) -> GetInvoiceResultSupplierInvoiceDocumentType:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
