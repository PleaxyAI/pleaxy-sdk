from typing import Literal, Set, cast

InvoiceActivityEntryKind = Literal[
    "approval",
    "approved",
    "comment",
    "control_findings",
    "corrects",
    "match",
    "payment",
    "received",
    "rejected",
    "reminder",
    "replacement",
    "sent_for_approval",
]

INVOICE_ACTIVITY_ENTRY_KIND_VALUES: Set[InvoiceActivityEntryKind] = {
    "approval",
    "approved",
    "comment",
    "control_findings",
    "corrects",
    "match",
    "payment",
    "received",
    "rejected",
    "reminder",
    "replacement",
    "sent_for_approval",
}


def check_invoice_activity_entry_kind(value: str) -> InvoiceActivityEntryKind:
    if value in INVOICE_ACTIVITY_ENTRY_KIND_VALUES:
        return cast(InvoiceActivityEntryKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_ACTIVITY_ENTRY_KIND_VALUES!r}"
    )
