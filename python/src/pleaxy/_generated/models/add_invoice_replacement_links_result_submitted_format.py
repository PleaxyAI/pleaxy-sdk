from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultSubmittedFormat = Literal["cxml", "json", "ubl"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SUBMITTED_FORMAT_VALUES: Set[
    AddInvoiceReplacementLinksResultSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_add_invoice_replacement_links_result_submitted_format(
    value: str,
) -> AddInvoiceReplacementLinksResultSubmittedFormat:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SUBMITTED_FORMAT_VALUES:
        return cast(AddInvoiceReplacementLinksResultSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SUBMITTED_FORMAT_VALUES!r}"
    )
