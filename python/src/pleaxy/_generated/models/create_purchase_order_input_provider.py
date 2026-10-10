from typing import Literal, Set, cast

CreatePurchaseOrderInputProvider = Literal["aws", "azure", "gcp", "oci"]

CREATE_PURCHASE_ORDER_INPUT_PROVIDER_VALUES: Set[CreatePurchaseOrderInputProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_purchase_order_input_provider(
    value: str,
) -> CreatePurchaseOrderInputProvider:
    if value in CREATE_PURCHASE_ORDER_INPUT_PROVIDER_VALUES:
        return cast(CreatePurchaseOrderInputProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PURCHASE_ORDER_INPUT_PROVIDER_VALUES!r}"
    )
