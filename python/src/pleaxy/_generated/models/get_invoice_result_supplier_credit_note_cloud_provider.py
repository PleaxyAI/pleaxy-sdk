from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteCloudProvider = Literal["aws", "azure", "gcp", "oci"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_get_invoice_result_supplier_credit_note_cloud_provider(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteCloudProvider:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
