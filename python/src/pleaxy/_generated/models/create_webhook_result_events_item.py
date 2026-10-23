from typing import Literal, Set, cast

CreateWebhookResultEventsItem = Literal[
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
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.updated",
]

CREATE_WEBHOOK_RESULT_EVENTS_ITEM_VALUES: Set[CreateWebhookResultEventsItem] = {
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
    "purchase_order.issued",
    "purchase_order.rejected",
    "purchase_order.updated",
}


def check_create_webhook_result_events_item(
    value: str,
) -> CreateWebhookResultEventsItem:
    if value in CREATE_WEBHOOK_RESULT_EVENTS_ITEM_VALUES:
        return cast(CreateWebhookResultEventsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WEBHOOK_RESULT_EVENTS_ITEM_VALUES!r}"
    )
