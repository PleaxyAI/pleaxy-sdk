from typing import Literal, Set, cast

CloudSetupViewState = Literal[
    "failed",
    "resumable",
    "start_over",
    "started_by_someone_else",
    "unavailable",
    "verifying",
]

CLOUD_SETUP_VIEW_STATE_VALUES: Set[CloudSetupViewState] = {
    "failed",
    "resumable",
    "start_over",
    "started_by_someone_else",
    "unavailable",
    "verifying",
}


def check_cloud_setup_view_state(value: str) -> CloudSetupViewState:
    if value in CLOUD_SETUP_VIEW_STATE_VALUES:
        return cast(CloudSetupViewState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_SETUP_VIEW_STATE_VALUES!r}"
    )
