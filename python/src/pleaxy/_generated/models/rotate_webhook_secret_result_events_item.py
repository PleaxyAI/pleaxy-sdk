from typing import Literal, Set, cast

RotateWebhookSecretResultEventsItem = Literal[
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
    "purchase_order.canceled",
    "purchase_order.changed",
    "purchase_order.confirmed",
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.shipped",
    "purchase_order.updated",
]

ROTATE_WEBHOOK_SECRET_RESULT_EVENTS_ITEM_VALUES: Set[
    RotateWebhookSecretResultEventsItem
] = {
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
    "purchase_order.canceled",
    "purchase_order.changed",
    "purchase_order.confirmed",
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.shipped",
    "purchase_order.updated",
}


def check_rotate_webhook_secret_result_events_item(
    value: str,
) -> RotateWebhookSecretResultEventsItem:
    if value in ROTATE_WEBHOOK_SECRET_RESULT_EVENTS_ITEM_VALUES:
        return cast(RotateWebhookSecretResultEventsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROTATE_WEBHOOK_SECRET_RESULT_EVENTS_ITEM_VALUES!r}"
    )
