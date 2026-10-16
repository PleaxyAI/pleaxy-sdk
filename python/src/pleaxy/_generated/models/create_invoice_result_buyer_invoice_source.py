from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceSource = Literal["direct", "feed", "manual", "po-flip"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_create_invoice_result_buyer_invoice_source(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceSource:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_SOURCE_VALUES!r}"
    )
