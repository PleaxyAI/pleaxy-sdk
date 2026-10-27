from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoicePaymentRoute = Literal["erp", "pleaxy"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    CreateInvoiceResultBuyerInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_create_invoice_result_buyer_invoice_payment_route(
    value: str,
) -> CreateInvoiceResultBuyerInvoicePaymentRoute:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
