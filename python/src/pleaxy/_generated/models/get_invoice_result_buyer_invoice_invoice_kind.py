from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceInvoiceKind = Literal["prepayment"]

GET_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES: Set[
    GetInvoiceResultBuyerInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_get_invoice_result_buyer_invoice_invoice_kind(
    value: str,
) -> GetInvoiceResultBuyerInvoiceInvoiceKind:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
