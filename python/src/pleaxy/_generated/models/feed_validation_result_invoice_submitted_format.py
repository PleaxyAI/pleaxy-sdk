from typing import Literal, Set, cast

FeedValidationResultInvoiceSubmittedFormat = Literal[
    "cii", "cxml", "facturae", "fatturapa", "json", "nfe", "nfse", "ubl"
]

FEED_VALIDATION_RESULT_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    FeedValidationResultInvoiceSubmittedFormat
] = {
    "cii",
    "cxml",
    "facturae",
    "fatturapa",
    "json",
    "nfe",
    "nfse",
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
