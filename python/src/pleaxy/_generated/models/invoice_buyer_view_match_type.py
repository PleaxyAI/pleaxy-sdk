from typing import Literal, Set, cast

InvoiceBuyerViewMatchType = Literal["three_way", "two_way", "usage"]

INVOICE_BUYER_VIEW_MATCH_TYPE_VALUES: Set[InvoiceBuyerViewMatchType] = {
    "three_way",
    "two_way",
    "usage",
}


def check_invoice_buyer_view_match_type(value: str) -> InvoiceBuyerViewMatchType:
    if value in INVOICE_BUYER_VIEW_MATCH_TYPE_VALUES:
        return cast(InvoiceBuyerViewMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_MATCH_TYPE_VALUES!r}"
    )
