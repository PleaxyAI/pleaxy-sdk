from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteCloudProvider = Literal[
    "aws", "azure", "gcp", "oci"
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_invoice_result_supplier_credit_note_cloud_provider(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteCloudProvider:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
