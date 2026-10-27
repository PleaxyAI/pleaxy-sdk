from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoicePaymentRoute = Literal["erp", "pleaxy"]

LIST_INVOICES_ITEM_BUYER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    ListInvoicesItemBuyerInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_list_invoices_item_buyer_invoice_payment_route(
    value: str,
) -> ListInvoicesItemBuyerInvoicePaymentRoute:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(ListInvoicesItemBuyerInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
