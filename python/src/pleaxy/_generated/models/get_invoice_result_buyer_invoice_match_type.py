from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceMatchType = Literal["three_way", "two_way", "usage"]

GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES: Set[
    GetInvoiceResultBuyerInvoiceMatchType
] = {
    "three_way",
    "two_way",
    "usage",
}


def check_get_invoice_result_buyer_invoice_match_type(
    value: str,
) -> GetInvoiceResultBuyerInvoiceMatchType:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES!r}"
    )
