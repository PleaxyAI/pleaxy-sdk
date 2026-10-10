from typing import Literal, Set, cast

SetInvoiceFeedResultType0FeedReadiness = Literal[
    "live", "no_key", "not_connected", "off", "tested", "untested"
]

SET_INVOICE_FEED_RESULT_TYPE_0_FEED_READINESS_VALUES: Set[
    SetInvoiceFeedResultType0FeedReadiness
] = {
    "live",
    "no_key",
    "not_connected",
    "off",
    "tested",
    "untested",
}


def check_set_invoice_feed_result_type_0_feed_readiness(
    value: str,
) -> SetInvoiceFeedResultType0FeedReadiness:
    if value in SET_INVOICE_FEED_RESULT_TYPE_0_FEED_READINESS_VALUES:
        return cast(SetInvoiceFeedResultType0FeedReadiness, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_0_FEED_READINESS_VALUES!r}"
    )
