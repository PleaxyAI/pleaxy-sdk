from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_invoice_result_supplier_invoice_cloud_provider(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceCloudProvider:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
