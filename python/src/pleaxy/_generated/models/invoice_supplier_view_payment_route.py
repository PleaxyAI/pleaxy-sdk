from typing import Literal, Set, cast

InvoiceSupplierViewPaymentRoute = Literal["erp", "pleaxy"]

INVOICE_SUPPLIER_VIEW_PAYMENT_ROUTE_VALUES: Set[InvoiceSupplierViewPaymentRoute] = {
    "erp",
    "pleaxy",
}


def check_invoice_supplier_view_payment_route(
    value: str,
) -> InvoiceSupplierViewPaymentRoute:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_ROUTE_VALUES:
        return cast(InvoiceSupplierViewPaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_ROUTE_VALUES!r}"
    )
