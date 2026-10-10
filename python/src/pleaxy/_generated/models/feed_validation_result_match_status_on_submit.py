from typing import Literal, Set, cast

FeedValidationResultMatchStatusOnSubmit = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

FEED_VALIDATION_RESULT_MATCH_STATUS_ON_SUBMIT_VALUES: Set[
    FeedValidationResultMatchStatusOnSubmit
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_feed_validation_result_match_status_on_submit(
    value: str,
) -> FeedValidationResultMatchStatusOnSubmit:
    if value in FEED_VALIDATION_RESULT_MATCH_STATUS_ON_SUBMIT_VALUES:
        return cast(FeedValidationResultMatchStatusOnSubmit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_MATCH_STATUS_ON_SUBMIT_VALUES!r}"
    )
