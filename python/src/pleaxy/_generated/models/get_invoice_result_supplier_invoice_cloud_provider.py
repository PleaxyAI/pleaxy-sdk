from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    GetInvoiceResultSupplierInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_get_invoice_result_supplier_invoice_cloud_provider(
    value: str,
) -> GetInvoiceResultSupplierInvoiceCloudProvider:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
