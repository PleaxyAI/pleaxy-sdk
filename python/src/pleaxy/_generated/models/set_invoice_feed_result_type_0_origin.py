from typing import Literal, Set, cast

SetInvoiceFeedResultType0Origin = Literal["rfq"]

SET_INVOICE_FEED_RESULT_TYPE_0_ORIGIN_VALUES: Set[SetInvoiceFeedResultType0Origin] = {
    "rfq",
}


def check_set_invoice_feed_result_type_0_origin(
    value: str,
) -> SetInvoiceFeedResultType0Origin:
    if value in SET_INVOICE_FEED_RESULT_TYPE_0_ORIGIN_VALUES:
        return cast(SetInvoiceFeedResultType0Origin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_0_ORIGIN_VALUES!r}"
    )
