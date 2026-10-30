from typing import Literal, Set, cast

AiProviderCreditPriceKind = Literal["capacity", "commit", "on_demand"]

AI_PROVIDER_CREDIT_PRICE_KIND_VALUES: Set[AiProviderCreditPriceKind] = {
    "capacity",
    "commit",
    "on_demand",
}


def check_ai_provider_credit_price_kind(value: str) -> AiProviderCreditPriceKind:
    if value in AI_PROVIDER_CREDIT_PRICE_KIND_VALUES:
        return cast(AiProviderCreditPriceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_CREDIT_PRICE_KIND_VALUES!r}"
    )
