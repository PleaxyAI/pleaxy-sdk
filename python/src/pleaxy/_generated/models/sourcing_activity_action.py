from typing import Literal, Set, cast

SourcingActivityAction = Literal[
    "answer_saved",
    "answer_submitted",
    "awarded",
    "canceled",
    "closed",
    "created",
    "deadline_moved",
    "declined",
    "edited",
    "invited",
    "published",
    "question_answered",
    "question_asked",
    "reopened",
    "round_opened",
    "scorecard_submitted",
    "scored",
    "viewed",
    "withdrawn",
]

SOURCING_ACTIVITY_ACTION_VALUES: Set[SourcingActivityAction] = {
    "answer_saved",
    "answer_submitted",
    "awarded",
    "canceled",
    "closed",
    "created",
    "deadline_moved",
    "declined",
    "edited",
    "invited",
    "published",
    "question_answered",
    "question_asked",
    "reopened",
    "round_opened",
    "scorecard_submitted",
    "scored",
    "viewed",
    "withdrawn",
}


def check_sourcing_activity_action(value: str) -> SourcingActivityAction:
    if value in SOURCING_ACTIVITY_ACTION_VALUES:
        return cast(SourcingActivityAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ACTIVITY_ACTION_VALUES!r}"
    )
