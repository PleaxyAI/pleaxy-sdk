from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceMatchBasis = Literal["purchase_order"]

GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES: Set[
    GetInvoiceResultBuyerInvoiceMatchBasis
] = {
    "purchase_order",
}


def check_get_invoice_result_buyer_invoice_match_basis(
    value: str,
) -> GetInvoiceResultBuyerInvoiceMatchBasis:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES!r}"
    )
