from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceSubmittedFormat = Literal["cxml", "json", "ubl"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_create_invoice_result_buyer_invoice_submitted_format(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceSubmittedFormat:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
