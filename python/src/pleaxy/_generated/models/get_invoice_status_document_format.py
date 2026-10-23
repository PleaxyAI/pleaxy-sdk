from typing import Literal, Set, cast

GetInvoiceStatusDocumentFormat = Literal["cxml", "ubl"]

GET_INVOICE_STATUS_DOCUMENT_FORMAT_VALUES: Set[GetInvoiceStatusDocumentFormat] = {
    "cxml",
    "ubl",
}


def check_get_invoice_status_document_format(
    value: str,
) -> GetInvoiceStatusDocumentFormat:
    if value in GET_INVOICE_STATUS_DOCUMENT_FORMAT_VALUES:
        return cast(GetInvoiceStatusDocumentFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_STATUS_DOCUMENT_FORMAT_VALUES!r}"
    )
