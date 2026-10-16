from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultEnteredBy = Literal["buyer", "supplier"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_ENTERED_BY_VALUES: Set[
    AddInvoiceReplacementLinksResultEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_add_invoice_replacement_links_result_entered_by(
    value: str,
) -> AddInvoiceReplacementLinksResultEnteredBy:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_ENTERED_BY_VALUES:
        return cast(AddInvoiceReplacementLinksResultEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_ENTERED_BY_VALUES!r}"
    )
