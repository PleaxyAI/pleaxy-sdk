from typing import Literal, Set, cast

FocusRunStatus = Literal["failed", "ok", "partial"]

FOCUS_RUN_STATUS_VALUES: Set[FocusRunStatus] = {
    "failed",
    "ok",
    "partial",
}


def check_focus_run_status(value: str) -> FocusRunStatus:
    if value in FOCUS_RUN_STATUS_VALUES:
        return cast(FocusRunStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_RUN_STATUS_VALUES!r}"
    )
