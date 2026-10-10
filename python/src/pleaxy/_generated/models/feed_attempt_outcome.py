from typing import Literal, Set, cast

FeedAttemptOutcome = Literal["accepted", "refused", "replayed", "valid"]

FEED_ATTEMPT_OUTCOME_VALUES: Set[FeedAttemptOutcome] = {
    "accepted",
    "refused",
    "replayed",
    "valid",
}


def check_feed_attempt_outcome(value: str) -> FeedAttemptOutcome:
    if value in FEED_ATTEMPT_OUTCOME_VALUES:
        return cast(FeedAttemptOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_ATTEMPT_OUTCOME_VALUES!r}"
    )
