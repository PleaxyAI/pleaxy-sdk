from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteSource = Literal["cloud_sync", "feed"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_create_invoice_result_buyer_credit_note_source(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteSource:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
