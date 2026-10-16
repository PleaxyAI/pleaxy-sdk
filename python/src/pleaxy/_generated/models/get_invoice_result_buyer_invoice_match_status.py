from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES: Set[
    GetInvoiceResultBuyerInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_get_invoice_result_buyer_invoice_match_status(
    value: str,
) -> GetInvoiceResultBuyerInvoiceMatchStatus:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
