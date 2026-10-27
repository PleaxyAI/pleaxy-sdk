from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoicePaymentRoute = Literal["erp", "pleaxy"]

GET_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    GetInvoiceResultBuyerInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_get_invoice_result_buyer_invoice_payment_route(
    value: str,
) -> GetInvoiceResultBuyerInvoicePaymentRoute:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(GetInvoiceResultBuyerInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
