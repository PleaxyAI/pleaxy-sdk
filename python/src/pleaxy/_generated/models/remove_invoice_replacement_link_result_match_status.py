from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_STATUS_VALUES: Set[
    RemoveInvoiceReplacementLinkResultMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_remove_invoice_replacement_link_result_match_status(
    value: str,
) -> RemoveInvoiceReplacementLinkResultMatchStatus:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_STATUS_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_STATUS_VALUES!r}"
    )
