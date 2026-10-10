from typing import Literal, Set, cast

InvoiceBuyerViewSubmittedFormat = Literal["cxml", "json", "ubl"]

INVOICE_BUYER_VIEW_SUBMITTED_FORMAT_VALUES: Set[InvoiceBuyerViewSubmittedFormat] = {
    "cxml",
    "json",
    "ubl",
}


def check_invoice_buyer_view_submitted_format(
    value: str,
) -> InvoiceBuyerViewSubmittedFormat:
    if value in INVOICE_BUYER_VIEW_SUBMITTED_FORMAT_VALUES:
        return cast(InvoiceBuyerViewSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_SUBMITTED_FORMAT_VALUES!r}"
    )
