from typing import Literal, Set, cast

InvoiceBuyerViewPaymentRoute = Literal["erp", "pleaxy"]

INVOICE_BUYER_VIEW_PAYMENT_ROUTE_VALUES: Set[InvoiceBuyerViewPaymentRoute] = {
    "erp",
    "pleaxy",
}


def check_invoice_buyer_view_payment_route(value: str) -> InvoiceBuyerViewPaymentRoute:
    if value in INVOICE_BUYER_VIEW_PAYMENT_ROUTE_VALUES:
        return cast(InvoiceBuyerViewPaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_PAYMENT_ROUTE_VALUES!r}"
    )
