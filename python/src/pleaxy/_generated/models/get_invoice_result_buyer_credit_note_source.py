from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteSource = Literal["cloud_sync", "feed"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_get_invoice_result_buyer_credit_note_source(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteSource:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
