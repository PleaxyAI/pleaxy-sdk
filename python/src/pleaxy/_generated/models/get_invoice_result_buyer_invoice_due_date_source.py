from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceDueDateSource = Literal["default", "stated"]

GET_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    GetInvoiceResultBuyerInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_get_invoice_result_buyer_invoice_due_date_source(
    value: str,
) -> GetInvoiceResultBuyerInvoiceDueDateSource:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
