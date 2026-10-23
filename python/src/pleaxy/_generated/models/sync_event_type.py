from typing import Literal, Set, cast

SyncEventType = Literal[
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

SYNC_EVENT_TYPE_VALUES: Set[SyncEventType] = {
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


def check_sync_event_type(value: str) -> SyncEventType:
    if value in SYNC_EVENT_TYPE_VALUES:
        return cast(SyncEventType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SYNC_EVENT_TYPE_VALUES!r}"
    )
