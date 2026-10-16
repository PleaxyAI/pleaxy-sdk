from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultDocumentType = Literal["debit_note", "invoice"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DOCUMENT_TYPE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_remove_invoice_replacement_link_result_document_type(
    value: str,
) -> RemoveInvoiceReplacementLinkResultDocumentType:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DOCUMENT_TYPE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DOCUMENT_TYPE_VALUES!r}"
    )
