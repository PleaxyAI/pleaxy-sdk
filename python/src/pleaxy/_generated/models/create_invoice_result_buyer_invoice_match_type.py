from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceMatchType = Literal["three_way", "two_way", "usage"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceMatchType
] = {
    "three_way",
    "two_way",
    "usage",
}


def check_create_invoice_result_buyer_invoice_match_type(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceMatchType:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_TYPE_VALUES!r}"
    )
