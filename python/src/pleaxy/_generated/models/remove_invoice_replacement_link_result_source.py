from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultSource = Literal[
    "direct", "feed", "manual", "po-flip"
]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SOURCE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_remove_invoice_replacement_link_result_source(
    value: str,
) -> RemoveInvoiceReplacementLinkResultSource:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SOURCE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SOURCE_VALUES!r}"
    )
