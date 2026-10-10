from typing import Literal, Set, cast

FeedAttemptMode = Literal["submit", "validate"]

FEED_ATTEMPT_MODE_VALUES: Set[FeedAttemptMode] = {
    "submit",
    "validate",
}


def check_feed_attempt_mode(value: str) -> FeedAttemptMode:
    if value in FEED_ATTEMPT_MODE_VALUES:
        return cast(FeedAttemptMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_ATTEMPT_MODE_VALUES!r}"
    )
