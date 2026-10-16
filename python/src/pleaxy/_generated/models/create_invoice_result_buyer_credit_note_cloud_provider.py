from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteCloudProvider = Literal["aws", "azure", "gcp", "oci"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_invoice_result_buyer_credit_note_cloud_provider(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteCloudProvider:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
