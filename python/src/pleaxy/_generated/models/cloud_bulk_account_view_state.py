from typing import Literal, Set, cast

CloudBulkAccountViewState = Literal["failed", "verifying"]

CLOUD_BULK_ACCOUNT_VIEW_STATE_VALUES: Set[CloudBulkAccountViewState] = {
    "failed",
    "verifying",
}


def check_cloud_bulk_account_view_state(value: str) -> CloudBulkAccountViewState:
    if value in CLOUD_BULK_ACCOUNT_VIEW_STATE_VALUES:
        return cast(CloudBulkAccountViewState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_BULK_ACCOUNT_VIEW_STATE_VALUES!r}"
    )
