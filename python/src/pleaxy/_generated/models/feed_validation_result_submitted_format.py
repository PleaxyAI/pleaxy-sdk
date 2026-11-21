from typing import Literal, Set, cast

FeedValidationResultSubmittedFormat = Literal["cii", "cxml", "fatturapa", "json", "ubl"]

FEED_VALIDATION_RESULT_SUBMITTED_FORMAT_VALUES: Set[
    FeedValidationResultSubmittedFormat
] = {
    "cii",
    "cxml",
    "fatturapa",
    "json",
    "ubl",
}


def check_feed_validation_result_submitted_format(
    value: str,
) -> FeedValidationResultSubmittedFormat:
    if value in FEED_VALIDATION_RESULT_SUBMITTED_FORMAT_VALUES:
        return cast(FeedValidationResultSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_SUBMITTED_FORMAT_VALUES!r}"
    )
