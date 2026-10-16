from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_get_invoice_result_buyer_credit_note_reason(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteReason:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES!r}"
    )
