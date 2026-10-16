from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultDueDateSource = Literal["default", "stated"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DUE_DATE_SOURCE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultDueDateSource
] = {
    "default",
    "stated",
}


def check_remove_invoice_replacement_link_result_due_date_source(
    value: str,
) -> RemoveInvoiceReplacementLinkResultDueDateSource:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DUE_DATE_SOURCE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_DUE_DATE_SOURCE_VALUES!r}"
    )
