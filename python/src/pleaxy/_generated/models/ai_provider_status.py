from typing import Literal, Set, cast

AiProviderStatus = Literal["connected", "pending"]

AI_PROVIDER_STATUS_VALUES: Set[AiProviderStatus] = {
    "connected",
    "pending",
}


def check_ai_provider_status(value: str) -> AiProviderStatus:
    if value in AI_PROVIDER_STATUS_VALUES:
        return cast(AiProviderStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_STATUS_VALUES!r}"
    )
