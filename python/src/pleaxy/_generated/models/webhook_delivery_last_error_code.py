from typing import Literal, Set, cast

WebhookDeliveryLastErrorCode = Literal[
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
]

WEBHOOK_DELIVERY_LAST_ERROR_CODE_VALUES: Set[WebhookDeliveryLastErrorCode] = {
    "blocked_address",
    "endpoint_off",
    "failed",
    "http_status",
    "redirect",
    "timeout",
    "too_large",
    "unreachable",
}


def check_webhook_delivery_last_error_code(value: str) -> WebhookDeliveryLastErrorCode:
    if value in WEBHOOK_DELIVERY_LAST_ERROR_CODE_VALUES:
        return cast(WebhookDeliveryLastErrorCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_LAST_ERROR_CODE_VALUES!r}"
    )
