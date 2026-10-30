from typing import Literal, Set, cast

AiProviderLastSyncErrorCode = Literal[
    "access_revoked", "data_not_enabled", "platform_config", "throttled", "unknown"
]

AI_PROVIDER_LAST_SYNC_ERROR_CODE_VALUES: Set[AiProviderLastSyncErrorCode] = {
    "access_revoked",
    "data_not_enabled",
    "platform_config",
    "throttled",
    "unknown",
}


def check_ai_provider_last_sync_error_code(value: str) -> AiProviderLastSyncErrorCode:
    if value in AI_PROVIDER_LAST_SYNC_ERROR_CODE_VALUES:
        return cast(AiProviderLastSyncErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_LAST_SYNC_ERROR_CODE_VALUES!r}"
    )
