from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceMatchBasis = Literal["no_po_history", "purchase_order"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceMatchBasis
] = {
    "no_po_history",
    "purchase_order",
}


def check_create_invoice_result_buyer_invoice_match_basis(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceMatchBasis:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_BASIS_VALUES!r}"
    )
