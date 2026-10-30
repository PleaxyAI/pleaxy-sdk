from typing import Literal, Set, cast

AiProviderLastSyncStatus = Literal["error", "ok", "throttled"]

AI_PROVIDER_LAST_SYNC_STATUS_VALUES: Set[AiProviderLastSyncStatus] = {
    "error",
    "ok",
    "throttled",
}


def check_ai_provider_last_sync_status(value: str) -> AiProviderLastSyncStatus:
    if value in AI_PROVIDER_LAST_SYNC_STATUS_VALUES:
        return cast(AiProviderLastSyncStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_LAST_SYNC_STATUS_VALUES!r}"
    )
