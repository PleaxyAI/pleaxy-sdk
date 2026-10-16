from typing import Literal, Set, cast

NotificationResolutionOutcome = Literal[
    "no_longer_needed", "you_approved", "you_rejected"
]

NOTIFICATION_RESOLUTION_OUTCOME_VALUES: Set[NotificationResolutionOutcome] = {
    "no_longer_needed",
    "you_approved",
    "you_rejected",
}


def check_notification_resolution_outcome(value: str) -> NotificationResolutionOutcome:
    if value in NOTIFICATION_RESOLUTION_OUTCOME_VALUES:
        return cast(NotificationResolutionOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_RESOLUTION_OUTCOME_VALUES!r}"
    )
