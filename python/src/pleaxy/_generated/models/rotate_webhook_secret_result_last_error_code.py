from typing import Literal, Set, cast

RotateWebhookSecretResultLastErrorCode = Literal[
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
]

ROTATE_WEBHOOK_SECRET_RESULT_LAST_ERROR_CODE_VALUES: Set[
    RotateWebhookSecretResultLastErrorCode
] = {
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
}


def check_rotate_webhook_secret_result_last_error_code(
    value: str,
) -> RotateWebhookSecretResultLastErrorCode:
    if value in ROTATE_WEBHOOK_SECRET_RESULT_LAST_ERROR_CODE_VALUES:
        return cast(RotateWebhookSecretResultLastErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROTATE_WEBHOOK_SECRET_RESULT_LAST_ERROR_CODE_VALUES!r}"
    )
