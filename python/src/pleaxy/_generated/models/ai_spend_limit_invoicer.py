from typing import Literal, Set, cast

AiSpendLimitInvoicer = Literal["anthropic", "aws", "azure", "gcp", "openai"]

AI_SPEND_LIMIT_INVOICER_VALUES: Set[AiSpendLimitInvoicer] = {
    "anthropic",
    "aws",
    "azure",
    "gcp",
    "openai",
}


def check_ai_spend_limit_invoicer(value: str) -> AiSpendLimitInvoicer:
    if value in AI_SPEND_LIMIT_INVOICER_VALUES:
        return cast(AiSpendLimitInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_LIMIT_INVOICER_VALUES!r}"
    )
