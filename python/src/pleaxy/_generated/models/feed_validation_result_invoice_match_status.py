from typing import Literal, Set, cast

FeedValidationResultInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

FEED_VALIDATION_RESULT_INVOICE_MATCH_STATUS_VALUES: Set[
    FeedValidationResultInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_feed_validation_result_invoice_match_status(
    value: str,
) -> FeedValidationResultInvoiceMatchStatus:
    if value in FEED_VALIDATION_RESULT_INVOICE_MATCH_STATUS_VALUES:
        return cast(FeedValidationResultInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_MATCH_STATUS_VALUES!r}"
    )
