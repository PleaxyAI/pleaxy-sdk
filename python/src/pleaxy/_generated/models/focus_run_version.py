from typing import Literal, Set, cast

FocusRunVersion = Literal["1.0", "1.1", "1.2", "1.3", "1.4"]

FOCUS_RUN_VERSION_VALUES: Set[FocusRunVersion] = {
    "1.0",
    "1.1",
    "1.2",
    "1.3",
    "1.4",
}


def check_focus_run_version(value: str) -> FocusRunVersion:
    if value in FOCUS_RUN_VERSION_VALUES:
        return cast(FocusRunVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_RUN_VERSION_VALUES!r}"
    )
