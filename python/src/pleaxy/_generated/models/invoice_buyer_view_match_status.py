from typing import Literal, Set, cast

InvoiceBuyerViewMatchStatus = Literal["discrepancy", "matched", "pending", "unverified"]

INVOICE_BUYER_VIEW_MATCH_STATUS_VALUES: Set[InvoiceBuyerViewMatchStatus] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_invoice_buyer_view_match_status(value: str) -> InvoiceBuyerViewMatchStatus:
    if value in INVOICE_BUYER_VIEW_MATCH_STATUS_VALUES:
        return cast(InvoiceBuyerViewMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_MATCH_STATUS_VALUES!r}"
    )
