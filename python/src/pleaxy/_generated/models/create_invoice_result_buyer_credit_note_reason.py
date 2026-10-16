from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_create_invoice_result_buyer_credit_note_reason(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteReason:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_REASON_VALUES!r}"
    )
