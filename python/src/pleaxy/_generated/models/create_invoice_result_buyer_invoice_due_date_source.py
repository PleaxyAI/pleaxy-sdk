from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceDueDateSource = Literal["default", "stated"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_create_invoice_result_buyer_invoice_due_date_source(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceDueDateSource:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
