from typing import Literal, Set, cast

InvoiceBuyerViewSource = Literal["cloud_sync", "direct", "feed", "manual", "po-flip"]

INVOICE_BUYER_VIEW_SOURCE_VALUES: Set[InvoiceBuyerViewSource] = {
    "cloud_sync",
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_invoice_buyer_view_source(value: str) -> InvoiceBuyerViewSource:
    if value in INVOICE_BUYER_VIEW_SOURCE_VALUES:
        return cast(InvoiceBuyerViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_SOURCE_VALUES!r}"
    )
