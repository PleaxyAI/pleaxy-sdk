from typing import Literal, Set, cast

InvoiceSourceDocumentContentType = Literal["application/pdf", "image/jpeg", "image/png"]

INVOICE_SOURCE_DOCUMENT_CONTENT_TYPE_VALUES: Set[InvoiceSourceDocumentContentType] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_invoice_source_document_content_type(
    value: str,
) -> InvoiceSourceDocumentContentType:
    if value in INVOICE_SOURCE_DOCUMENT_CONTENT_TYPE_VALUES:
        return cast(InvoiceSourceDocumentContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SOURCE_DOCUMENT_CONTENT_TYPE_VALUES!r}"
    )
