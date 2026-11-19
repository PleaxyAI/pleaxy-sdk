from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_invoice_result_buyer_invoice_cloud_provider(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceCloudProvider:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
