from typing import Literal, Set, cast

WebhookDeliveryStatus = Literal["delivered", "failed", "pending"]

WEBHOOK_DELIVERY_STATUS_VALUES: Set[WebhookDeliveryStatus] = {
    "delivered",
    "failed",
    "pending",
}


def check_webhook_delivery_status(value: str) -> WebhookDeliveryStatus:
    if value in WEBHOOK_DELIVERY_STATUS_VALUES:
        return cast(WebhookDeliveryStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_STATUS_VALUES!r}"
    )
