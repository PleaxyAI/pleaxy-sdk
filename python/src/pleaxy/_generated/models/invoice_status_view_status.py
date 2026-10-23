from typing import Literal, Set, cast

InvoiceStatusViewStatus = Literal[
    "approved",
    "duplicate",
    "in_process",
    "paid",
    "payment_in_progress",
    "received",
    "rejected",
    "under_query",
]

INVOICE_STATUS_VIEW_STATUS_VALUES: Set[InvoiceStatusViewStatus] = {
    "approved",
    "duplicate",
    "in_process",
    "paid",
    "payment_in_progress",
    "received",
    "rejected",
    "under_query",
}


def check_invoice_status_view_status(value: str) -> InvoiceStatusViewStatus:
    if value in INVOICE_STATUS_VIEW_STATUS_VALUES:
        return cast(InvoiceStatusViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_STATUS_VALUES!r}"
    )
