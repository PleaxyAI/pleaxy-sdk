from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceEnteredBy = Literal["buyer", "supplier"]

GET_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES: Set[
    GetInvoiceResultBuyerInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_get_invoice_result_buyer_invoice_entered_by(
    value: str,
) -> GetInvoiceResultBuyerInvoiceEnteredBy:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES!r}"
    )
