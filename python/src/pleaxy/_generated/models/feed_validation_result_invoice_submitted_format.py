from typing import Literal, Set, cast

FeedValidationResultInvoiceSubmittedFormat = Literal["cxml", "json", "ubl"]

FEED_VALIDATION_RESULT_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    FeedValidationResultInvoiceSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_feed_validation_result_invoice_submitted_format(
    value: str,
) -> FeedValidationResultInvoiceSubmittedFormat:
    if value in FEED_VALIDATION_RESULT_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(FeedValidationResultInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
