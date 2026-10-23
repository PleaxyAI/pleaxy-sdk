from typing import Literal, Set, cast

ConvertPurchaseRequestInputProvider = Literal["aws", "azure", "gcp", "oci"]

CONVERT_PURCHASE_REQUEST_INPUT_PROVIDER_VALUES: Set[
    ConvertPurchaseRequestInputProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_convert_purchase_request_input_provider(
    value: str,
) -> ConvertPurchaseRequestInputProvider:
    if value in CONVERT_PURCHASE_REQUEST_INPUT_PROVIDER_VALUES:
        return cast(ConvertPurchaseRequestInputProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERT_PURCHASE_REQUEST_INPUT_PROVIDER_VALUES!r}"
    )
