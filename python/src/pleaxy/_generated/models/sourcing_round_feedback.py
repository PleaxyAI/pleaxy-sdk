from typing import Literal, Set, cast

SourcingRoundFeedback = Literal["gap", "none", "rank"]

SOURCING_ROUND_FEEDBACK_VALUES: Set[SourcingRoundFeedback] = {
    "gap",
    "none",
    "rank",
}


def check_sourcing_round_feedback(value: str) -> SourcingRoundFeedback:
    if value in SOURCING_ROUND_FEEDBACK_VALUES:
        return cast(SourcingRoundFeedback, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ROUND_FEEDBACK_VALUES!r}"
    )
