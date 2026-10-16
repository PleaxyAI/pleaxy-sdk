from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceInvoiceKind = Literal["prepayment"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_create_invoice_result_buyer_invoice_invoice_kind(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceInvoiceKind:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
