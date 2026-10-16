from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteCloudProvider = Literal["aws", "azure", "gcp", "oci"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_get_invoice_result_buyer_credit_note_cloud_provider(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteCloudProvider:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
