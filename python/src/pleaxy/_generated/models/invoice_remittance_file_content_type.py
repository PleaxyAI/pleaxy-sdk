from typing import Literal, Set, cast

InvoiceRemittanceFileContentType = Literal["application/pdf", "image/jpeg", "image/png"]

INVOICE_REMITTANCE_FILE_CONTENT_TYPE_VALUES: Set[InvoiceRemittanceFileContentType] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_invoice_remittance_file_content_type(
    value: str,
) -> InvoiceRemittanceFileContentType:
    if value in INVOICE_REMITTANCE_FILE_CONTENT_TYPE_VALUES:
        return cast(InvoiceRemittanceFileContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_REMITTANCE_FILE_CONTENT_TYPE_VALUES!r}"
    )
