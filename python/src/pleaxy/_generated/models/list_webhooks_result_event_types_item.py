from typing import Literal, Set, cast

ListWebhooksResultEventTypesItem = Literal[
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

LIST_WEBHOOKS_RESULT_EVENT_TYPES_ITEM_VALUES: Set[ListWebhooksResultEventTypesItem] = {
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


def check_list_webhooks_result_event_types_item(
    value: str,
) -> ListWebhooksResultEventTypesItem:
    if value in LIST_WEBHOOKS_RESULT_EVENT_TYPES_ITEM_VALUES:
        return cast(ListWebhooksResultEventTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOKS_RESULT_EVENT_TYPES_ITEM_VALUES!r}"
    )
