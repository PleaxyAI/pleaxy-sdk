from typing import Literal, Set, cast

WebhookEndpointViewLastErrorCode = Literal[
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
]

WEBHOOK_ENDPOINT_VIEW_LAST_ERROR_CODE_VALUES: Set[WebhookEndpointViewLastErrorCode] = {
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
}


def check_webhook_endpoint_view_last_error_code(
    value: str,
) -> WebhookEndpointViewLastErrorCode:
    if value in WEBHOOK_ENDPOINT_VIEW_LAST_ERROR_CODE_VALUES:
        return cast(WebhookEndpointViewLastErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_ENDPOINT_VIEW_LAST_ERROR_CODE_VALUES!r}"
    )
