from typing import Literal, Set, cast

CloudConnectionLastSyncStatus = Literal["error", "never", "ok", "throttled"]

CLOUD_CONNECTION_LAST_SYNC_STATUS_VALUES: Set[CloudConnectionLastSyncStatus] = {
    "error",
    "never",
    "ok",
    "throttled",
}


def check_cloud_connection_last_sync_status(
    value: str,
) -> CloudConnectionLastSyncStatus:
    if value in CLOUD_CONNECTION_LAST_SYNC_STATUS_VALUES:
        return cast(CloudConnectionLastSyncStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_LAST_SYNC_STATUS_VALUES!r}"
    )
