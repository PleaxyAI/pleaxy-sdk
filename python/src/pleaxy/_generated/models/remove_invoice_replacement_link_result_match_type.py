from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultMatchType = Literal["three_way", "two_way", "usage"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_TYPE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultMatchType
] = {
    "three_way",
    "two_way",
    "usage",
}


def check_remove_invoice_replacement_link_result_match_type(
    value: str,
) -> RemoveInvoiceReplacementLinkResultMatchType:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_TYPE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_TYPE_VALUES!r}"
    )
