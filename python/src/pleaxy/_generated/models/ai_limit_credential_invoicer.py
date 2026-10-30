from typing import Literal, Set, cast

AiLimitCredentialInvoicer = Literal["anthropic", "aws", "azure", "gcp", "openai"]

AI_LIMIT_CREDENTIAL_INVOICER_VALUES: Set[AiLimitCredentialInvoicer] = {
    "anthropic",
    "aws",
    "azure",
    "gcp",
    "openai",
}


def check_ai_limit_credential_invoicer(value: str) -> AiLimitCredentialInvoicer:
    if value in AI_LIMIT_CREDENTIAL_INVOICER_VALUES:
        return cast(AiLimitCredentialInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LIMIT_CREDENTIAL_INVOICER_VALUES!r}"
    )
