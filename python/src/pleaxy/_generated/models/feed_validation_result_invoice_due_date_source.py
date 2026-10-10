from typing import Literal, Set, cast

FeedValidationResultInvoiceDueDateSource = Literal["default", "stated"]

FEED_VALIDATION_RESULT_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    FeedValidationResultInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_feed_validation_result_invoice_due_date_source(
    value: str,
) -> FeedValidationResultInvoiceDueDateSource:
    if value in FEED_VALIDATION_RESULT_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(FeedValidationResultInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
