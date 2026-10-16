from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_create_invoice_result_buyer_invoice_match_status(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceMatchStatus:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
