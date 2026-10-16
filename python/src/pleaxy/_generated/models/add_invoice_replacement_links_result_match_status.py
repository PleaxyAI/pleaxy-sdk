from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_STATUS_VALUES: Set[
    AddInvoiceReplacementLinksResultMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_add_invoice_replacement_links_result_match_status(
    value: str,
) -> AddInvoiceReplacementLinksResultMatchStatus:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_STATUS_VALUES:
        return cast(AddInvoiceReplacementLinksResultMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_STATUS_VALUES!r}"
    )
