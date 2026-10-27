from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoicePaymentRoute = Literal["erp", "pleaxy"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    ListInvoicesItemSupplierInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_list_invoices_item_supplier_invoice_payment_route(
    value: str,
) -> ListInvoicesItemSupplierInvoicePaymentRoute:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(ListInvoicesItemSupplierInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
