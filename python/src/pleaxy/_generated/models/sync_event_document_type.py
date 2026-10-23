from typing import Literal, Set, cast

SyncEventDocumentType = Literal["credit_note", "invoice", "purchase_order"]

SYNC_EVENT_DOCUMENT_TYPE_VALUES: Set[SyncEventDocumentType] = {
    "credit_note",
    "invoice",
    "purchase_order",
}


def check_sync_event_document_type(value: str) -> SyncEventDocumentType:
    if value in SYNC_EVENT_DOCUMENT_TYPE_VALUES:
        return cast(SyncEventDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SYNC_EVENT_DOCUMENT_TYPE_VALUES!r}"
    )
