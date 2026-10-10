from typing import Literal, Set, cast

SetInvoiceFeedResultType1Status = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

SET_INVOICE_FEED_RESULT_TYPE_1_STATUS_VALUES: Set[SetInvoiceFeedResultType1Status] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_set_invoice_feed_result_type_1_status(
    value: str,
) -> SetInvoiceFeedResultType1Status:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_STATUS_VALUES:
        return cast(SetInvoiceFeedResultType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_STATUS_VALUES!r}"
    )
