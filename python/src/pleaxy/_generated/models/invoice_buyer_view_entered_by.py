from typing import Literal, Set, cast

InvoiceBuyerViewEnteredBy = Literal["buyer", "supplier"]

INVOICE_BUYER_VIEW_ENTERED_BY_VALUES: Set[InvoiceBuyerViewEnteredBy] = {
    "buyer",
    "supplier",
}


def check_invoice_buyer_view_entered_by(value: str) -> InvoiceBuyerViewEnteredBy:
    if value in INVOICE_BUYER_VIEW_ENTERED_BY_VALUES:
        return cast(InvoiceBuyerViewEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_ENTERED_BY_VALUES!r}"
    )
