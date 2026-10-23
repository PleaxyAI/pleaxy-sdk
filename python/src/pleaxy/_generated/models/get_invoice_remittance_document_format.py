from typing import Literal, Set, cast

GetInvoiceRemittanceDocumentFormat = Literal["cxml", "ubl"]

GET_INVOICE_REMITTANCE_DOCUMENT_FORMAT_VALUES: Set[
    GetInvoiceRemittanceDocumentFormat
] = {
    "cxml",
    "ubl",
}


def check_get_invoice_remittance_document_format(
    value: str,
) -> GetInvoiceRemittanceDocumentFormat:
    if value in GET_INVOICE_REMITTANCE_DOCUMENT_FORMAT_VALUES:
        return cast(GetInvoiceRemittanceDocumentFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_REMITTANCE_DOCUMENT_FORMAT_VALUES!r}"
    )
