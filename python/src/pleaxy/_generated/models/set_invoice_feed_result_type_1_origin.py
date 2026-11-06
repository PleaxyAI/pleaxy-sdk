from typing import Literal, Set, cast

SetInvoiceFeedResultType1Origin = Literal["rfq"]

SET_INVOICE_FEED_RESULT_TYPE_1_ORIGIN_VALUES: Set[SetInvoiceFeedResultType1Origin] = {
    "rfq",
}


def check_set_invoice_feed_result_type_1_origin(
    value: str,
) -> SetInvoiceFeedResultType1Origin:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_ORIGIN_VALUES:
        return cast(SetInvoiceFeedResultType1Origin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_ORIGIN_VALUES!r}"
    )
