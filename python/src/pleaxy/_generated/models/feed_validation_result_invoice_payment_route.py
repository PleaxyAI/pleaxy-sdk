from typing import Literal, Set, cast

FeedValidationResultInvoicePaymentRoute = Literal["erp", "pleaxy"]

FEED_VALIDATION_RESULT_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    FeedValidationResultInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_feed_validation_result_invoice_payment_route(
    value: str,
) -> FeedValidationResultInvoicePaymentRoute:
    if value in FEED_VALIDATION_RESULT_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(FeedValidationResultInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
