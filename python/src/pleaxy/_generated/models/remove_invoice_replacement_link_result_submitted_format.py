from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultSubmittedFormat = Literal["cxml", "json", "ubl"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SUBMITTED_FORMAT_VALUES: Set[
    RemoveInvoiceReplacementLinkResultSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_remove_invoice_replacement_link_result_submitted_format(
    value: str,
) -> RemoveInvoiceReplacementLinkResultSubmittedFormat:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SUBMITTED_FORMAT_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_SUBMITTED_FORMAT_VALUES!r}"
    )
