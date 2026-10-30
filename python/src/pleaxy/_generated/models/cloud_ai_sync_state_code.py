from typing import Literal, Set, cast

CloudAiSyncStateCode = Literal[
    "access_revoked", "data_not_enabled", "platform_config", "throttled", "unknown"
]

CLOUD_AI_SYNC_STATE_CODE_VALUES: Set[CloudAiSyncStateCode] = {
    "access_revoked",
    "data_not_enabled",
    "platform_config",
    "throttled",
    "unknown",
}


def check_cloud_ai_sync_state_code(value: str) -> CloudAiSyncStateCode:
    if value in CLOUD_AI_SYNC_STATE_CODE_VALUES:
        return cast(CloudAiSyncStateCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_AI_SYNC_STATE_CODE_VALUES!r}"
    )
