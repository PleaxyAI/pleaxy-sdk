from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceDiscrepancyReason = Literal[
    "amount", "controls", "currency"
]

GET_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES: Set[
    GetInvoiceResultBuyerInvoiceDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
}


def check_get_invoice_result_buyer_invoice_discrepancy_reason(
    value: str,
) -> GetInvoiceResultBuyerInvoiceDiscrepancyReason:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES!r}"
    )
