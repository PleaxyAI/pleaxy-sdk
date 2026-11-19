from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

GET_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    GetInvoiceResultBuyerInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_get_invoice_result_buyer_invoice_cloud_provider(
    value: str,
) -> GetInvoiceResultBuyerInvoiceCloudProvider:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
