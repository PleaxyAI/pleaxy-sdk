from typing import Literal, Set, cast

CloudAiSyncStateStatus = Literal["error", "ok", "throttled"]

CLOUD_AI_SYNC_STATE_STATUS_VALUES: Set[CloudAiSyncStateStatus] = {
    "error",
    "ok",
    "throttled",
}


def check_cloud_ai_sync_state_status(value: str) -> CloudAiSyncStateStatus:
    if value in CLOUD_AI_SYNC_STATE_STATUS_VALUES:
        return cast(CloudAiSyncStateStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_AI_SYNC_STATE_STATUS_VALUES!r}"
    )
