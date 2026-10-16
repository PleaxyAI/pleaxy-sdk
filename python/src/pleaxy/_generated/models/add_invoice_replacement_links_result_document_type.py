from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultDocumentType = Literal["debit_note", "invoice"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DOCUMENT_TYPE_VALUES: Set[
    AddInvoiceReplacementLinksResultDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_add_invoice_replacement_links_result_document_type(
    value: str,
) -> AddInvoiceReplacementLinksResultDocumentType:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DOCUMENT_TYPE_VALUES:
        return cast(AddInvoiceReplacementLinksResultDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DOCUMENT_TYPE_VALUES!r}"
    )
