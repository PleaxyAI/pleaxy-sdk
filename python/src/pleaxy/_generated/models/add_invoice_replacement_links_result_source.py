from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultSource = Literal["direct", "feed", "manual", "po-flip"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SOURCE_VALUES: Set[
    AddInvoiceReplacementLinksResultSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_add_invoice_replacement_links_result_source(
    value: str,
) -> AddInvoiceReplacementLinksResultSource:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SOURCE_VALUES:
        return cast(AddInvoiceReplacementLinksResultSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_SOURCE_VALUES!r}"
    )
