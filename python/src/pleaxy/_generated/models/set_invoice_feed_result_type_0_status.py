from typing import Literal, Set, cast

SetInvoiceFeedResultType0Status = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

SET_INVOICE_FEED_RESULT_TYPE_0_STATUS_VALUES: Set[SetInvoiceFeedResultType0Status] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_set_invoice_feed_result_type_0_status(
    value: str,
) -> SetInvoiceFeedResultType0Status:
    if value in SET_INVOICE_FEED_RESULT_TYPE_0_STATUS_VALUES:
        return cast(SetInvoiceFeedResultType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_0_STATUS_VALUES!r}"
    )
