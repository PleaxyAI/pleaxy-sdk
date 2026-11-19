from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceSource = Literal[
    "cloud_sync", "direct", "feed", "manual", "po-flip"
]

GET_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES: Set[
    GetInvoiceResultBuyerInvoiceSource
] = {
    "cloud_sync",
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_get_invoice_result_buyer_invoice_source(
    value: str,
) -> GetInvoiceResultBuyerInvoiceSource:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES!r}"
    )
