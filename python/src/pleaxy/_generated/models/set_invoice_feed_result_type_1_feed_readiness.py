from typing import Literal, Set, cast

SetInvoiceFeedResultType1FeedReadiness = Literal[
    "live", "no_key", "not_connected", "off", "tested", "untested"
]

SET_INVOICE_FEED_RESULT_TYPE_1_FEED_READINESS_VALUES: Set[
    SetInvoiceFeedResultType1FeedReadiness
] = {
    "live",
    "no_key",
    "not_connected",
    "off",
    "tested",
    "untested",
}


def check_set_invoice_feed_result_type_1_feed_readiness(
    value: str,
) -> SetInvoiceFeedResultType1FeedReadiness:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_FEED_READINESS_VALUES:
        return cast(SetInvoiceFeedResultType1FeedReadiness, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_FEED_READINESS_VALUES!r}"
    )
