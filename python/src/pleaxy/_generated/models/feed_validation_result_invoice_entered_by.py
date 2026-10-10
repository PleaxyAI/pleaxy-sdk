from typing import Literal, Set, cast

FeedValidationResultInvoiceEnteredBy = Literal["buyer", "supplier"]

FEED_VALIDATION_RESULT_INVOICE_ENTERED_BY_VALUES: Set[
    FeedValidationResultInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_feed_validation_result_invoice_entered_by(
    value: str,
) -> FeedValidationResultInvoiceEnteredBy:
    if value in FEED_VALIDATION_RESULT_INVOICE_ENTERED_BY_VALUES:
        return cast(FeedValidationResultInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_ENTERED_BY_VALUES!r}"
    )
