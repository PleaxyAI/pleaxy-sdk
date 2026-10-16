from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceEnteredBy = Literal["buyer", "supplier"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_create_invoice_result_buyer_invoice_entered_by(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceEnteredBy:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_ENTERED_BY_VALUES!r}"
    )
