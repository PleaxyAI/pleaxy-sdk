from typing import Literal, Set, cast

FocusRunFailureReason = Literal[
    "accessDenied",
    "connectionMissing",
    "credentialRejected",
    "notFocus",
    "notFound",
    "other",
    "parquetUnsupported",
    "unreachable",
    "wrongRegion",
]

FOCUS_RUN_FAILURE_REASON_VALUES: Set[FocusRunFailureReason] = {
    "accessDenied",
    "connectionMissing",
    "credentialRejected",
    "notFocus",
    "notFound",
    "other",
    "parquetUnsupported",
    "unreachable",
    "wrongRegion",
}


def check_focus_run_failure_reason(value: str) -> FocusRunFailureReason:
    if value in FOCUS_RUN_FAILURE_REASON_VALUES:
        return cast(FocusRunFailureReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_RUN_FAILURE_REASON_VALUES!r}"
    )
