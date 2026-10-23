from typing import Literal, Set, cast

InvoiceStatusViewQueryReason = Literal[
    "bank_details_disputed", "bank_details_unconfirmed", "discrepancy"
]

INVOICE_STATUS_VIEW_QUERY_REASON_VALUES: Set[InvoiceStatusViewQueryReason] = {
    "bank_details_disputed",
    "bank_details_unconfirmed",
    "discrepancy",
}


def check_invoice_status_view_query_reason(value: str) -> InvoiceStatusViewQueryReason:
    if value in INVOICE_STATUS_VIEW_QUERY_REASON_VALUES:
        return cast(InvoiceStatusViewQueryReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_QUERY_REASON_VALUES!r}"
    )
