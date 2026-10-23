from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultMatchType = Literal["three_way", "two_way", "usage"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_TYPE_VALUES: Set[
    AddInvoiceReplacementLinksResultMatchType
] = {
    "three_way",
    "two_way",
    "usage",
}


def check_add_invoice_replacement_links_result_match_type(
    value: str,
) -> AddInvoiceReplacementLinksResultMatchType:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_TYPE_VALUES:
        return cast(AddInvoiceReplacementLinksResultMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_TYPE_VALUES!r}"
    )
