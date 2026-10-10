from typing import Literal, Set, cast

CloudConnectionStatus = Literal["connected", "error", "pending"]

CLOUD_CONNECTION_STATUS_VALUES: Set[CloudConnectionStatus] = {
    "connected",
    "error",
    "pending",
}


def check_cloud_connection_status(value: str) -> CloudConnectionStatus:
    if value in CLOUD_CONNECTION_STATUS_VALUES:
        return cast(CloudConnectionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_STATUS_VALUES!r}"
    )
