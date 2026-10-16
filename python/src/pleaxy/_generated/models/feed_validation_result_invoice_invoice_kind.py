from typing import Literal, Set, cast

FeedValidationResultInvoiceInvoiceKind = Literal["prepayment"]

FEED_VALIDATION_RESULT_INVOICE_INVOICE_KIND_VALUES: Set[
    FeedValidationResultInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_feed_validation_result_invoice_invoice_kind(
    value: str,
) -> FeedValidationResultInvoiceInvoiceKind:
    if value in FEED_VALIDATION_RESULT_INVOICE_INVOICE_KIND_VALUES:
        return cast(FeedValidationResultInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_INVOICE_KIND_VALUES!r}"
    )
