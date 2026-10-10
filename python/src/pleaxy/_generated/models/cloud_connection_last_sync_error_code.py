from typing import Literal, Set, cast

CloudConnectionLastSyncErrorCode = Literal[
    "access_revoked", "data_not_enabled", "platform_config", "throttled", "unknown"
]

CLOUD_CONNECTION_LAST_SYNC_ERROR_CODE_VALUES: Set[CloudConnectionLastSyncErrorCode] = {
    "access_revoked",
    "data_not_enabled",
    "platform_config",
    "throttled",
    "unknown",
}


def check_cloud_connection_last_sync_error_code(
    value: str,
) -> CloudConnectionLastSyncErrorCode:
    if value in CLOUD_CONNECTION_LAST_SYNC_ERROR_CODE_VALUES:
        return cast(CloudConnectionLastSyncErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_LAST_SYNC_ERROR_CODE_VALUES!r}"
    )
