from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceDiscrepancyReason = Literal[
    "amount", "controls", "currency"
]

CREATE_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
}


def check_create_invoice_result_buyer_invoice_discrepancy_reason(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceDiscrepancyReason:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_DISCREPANCY_REASON_VALUES!r}"
    )
