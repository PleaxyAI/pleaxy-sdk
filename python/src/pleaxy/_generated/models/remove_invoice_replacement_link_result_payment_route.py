from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultPaymentRoute = Literal["erp", "pleaxy"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_PAYMENT_ROUTE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultPaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_remove_invoice_replacement_link_result_payment_route(
    value: str,
) -> RemoveInvoiceReplacementLinkResultPaymentRoute:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_PAYMENT_ROUTE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultPaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_PAYMENT_ROUTE_VALUES!r}"
    )
