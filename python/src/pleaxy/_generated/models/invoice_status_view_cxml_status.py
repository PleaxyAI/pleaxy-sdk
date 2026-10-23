from typing import Literal, Set, cast

InvoiceStatusViewCxmlStatus = Literal[
    "paid", "paying", "processing", "reconciled", "rejected"
]

INVOICE_STATUS_VIEW_CXML_STATUS_VALUES: Set[InvoiceStatusViewCxmlStatus] = {
    "paid",
    "paying",
    "processing",
    "reconciled",
    "rejected",
}


def check_invoice_status_view_cxml_status(value: str) -> InvoiceStatusViewCxmlStatus:
    if value in INVOICE_STATUS_VIEW_CXML_STATUS_VALUES:
        return cast(InvoiceStatusViewCxmlStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_CXML_STATUS_VALUES!r}"
    )
