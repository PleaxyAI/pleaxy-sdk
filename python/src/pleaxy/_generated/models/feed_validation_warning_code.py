from typing import Literal, Set, cast

FeedValidationWarningCode = Literal["FEED_NOT_ENABLED", "RATE_DIFFERS"]

FEED_VALIDATION_WARNING_CODE_VALUES: Set[FeedValidationWarningCode] = {
    "FEED_NOT_ENABLED",
    "RATE_DIFFERS",
}


def check_feed_validation_warning_code(value: str) -> FeedValidationWarningCode:
    if value in FEED_VALIDATION_WARNING_CODE_VALUES:
        return cast(FeedValidationWarningCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_WARNING_CODE_VALUES!r}"
    )
