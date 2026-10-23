from typing import Literal, Set, cast

CreateWebhookResultLastErrorCode = Literal[
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
]

CREATE_WEBHOOK_RESULT_LAST_ERROR_CODE_VALUES: Set[CreateWebhookResultLastErrorCode] = {
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
}


def check_create_webhook_result_last_error_code(
    value: str,
) -> CreateWebhookResultLastErrorCode:
    if value in CREATE_WEBHOOK_RESULT_LAST_ERROR_CODE_VALUES:
        return cast(CreateWebhookResultLastErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBHOOK_RESULT_LAST_ERROR_CODE_VALUES!r}"
    )
