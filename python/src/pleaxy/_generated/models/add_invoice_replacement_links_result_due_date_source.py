from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultDueDateSource = Literal["default", "stated"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DUE_DATE_SOURCE_VALUES: Set[
    AddInvoiceReplacementLinksResultDueDateSource
] = {
    "default",
    "stated",
}


def check_add_invoice_replacement_links_result_due_date_source(
    value: str,
) -> AddInvoiceReplacementLinksResultDueDateSource:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DUE_DATE_SOURCE_VALUES:
        return cast(AddInvoiceReplacementLinksResultDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DUE_DATE_SOURCE_VALUES!r}"
    )
