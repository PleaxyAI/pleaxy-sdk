from typing import Literal, Set, cast

WebhookEndpointViewEventsItem = Literal[
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

WEBHOOK_ENDPOINT_VIEW_EVENTS_ITEM_VALUES: Set[WebhookEndpointViewEventsItem] = {
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


def check_webhook_endpoint_view_events_item(
    value: str,
) -> WebhookEndpointViewEventsItem:
    if value in WEBHOOK_ENDPOINT_VIEW_EVENTS_ITEM_VALUES:
        return cast(WebhookEndpointViewEventsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_ENDPOINT_VIEW_EVENTS_ITEM_VALUES!r}"
    )
