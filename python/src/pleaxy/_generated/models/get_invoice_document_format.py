from typing import Literal, Set, cast

GetInvoiceDocumentFormat = Literal["ubl"]

GET_INVOICE_DOCUMENT_FORMAT_VALUES: Set[GetInvoiceDocumentFormat] = {
    "ubl",
}


def check_get_invoice_document_format(value: str) -> GetInvoiceDocumentFormat:
    if value in GET_INVOICE_DOCUMENT_FORMAT_VALUES:
        return cast(GetInvoiceDocumentFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_DOCUMENT_FORMAT_VALUES!r}"
    )
