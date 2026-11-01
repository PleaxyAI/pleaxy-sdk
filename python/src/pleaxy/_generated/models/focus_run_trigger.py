from typing import Literal, Set, cast

FocusRunTrigger = Literal["manual", "schedule", "upload"]

FOCUS_RUN_TRIGGER_VALUES: Set[FocusRunTrigger] = {
    "manual",
    "schedule",
    "upload",
}


def check_focus_run_trigger(value: str) -> FocusRunTrigger:
    if value in FOCUS_RUN_TRIGGER_VALUES:
        return cast(FocusRunTrigger, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_RUN_TRIGGER_VALUES!r}"
    )
