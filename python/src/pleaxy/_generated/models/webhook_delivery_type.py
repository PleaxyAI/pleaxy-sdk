from typing import Literal, Set, cast

WebhookDeliveryType = Literal[
    "credit_note.accepted",
    "credit_note.received",
    "credit_note.rejected",
    "invoice.approved",
    "invoice.credit_applied",
    "invoice.paid",
    "invoice.payment_failed",
    "invoice.payment_withdrawn",
    "invoice.received",
    "invoice.rejected",
    "invoice.remittance_sent",
    "invoice.updated",
    "ping",
    "purchase_order.canceled",
    "purchase_order.changed",
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.updated",
]

WEBHOOK_DELIVERY_TYPE_VALUES: Set[WebhookDeliveryType] = {
    "credit_note.accepted",
    "credit_note.received",
    "credit_note.rejected",
    "invoice.approved",
    "invoice.credit_applied",
    "invoice.paid",
    "invoice.payment_failed",
    "invoice.payment_withdrawn",
    "invoice.received",
    "invoice.rejected",
    "invoice.remittance_sent",
    "invoice.updated",
    "ping",
    "purchase_order.canceled",
    "purchase_order.changed",
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.updated",
}


def check_webhook_delivery_type(value: str) -> WebhookDeliveryType:
    if value in WEBHOOK_DELIVERY_TYPE_VALUES:
        return cast(WebhookDeliveryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_TYPE_VALUES!r}"
    )
