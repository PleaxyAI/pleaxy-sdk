from typing import Literal, Set, cast

PurchaseOrderProvider = Literal["aws", "azure", "gcp", "oci"]

PURCHASE_ORDER_PROVIDER_VALUES: Set[PurchaseOrderProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_purchase_order_provider(value: str) -> PurchaseOrderProvider:
    if value in PURCHASE_ORDER_PROVIDER_VALUES:
        return cast(PurchaseOrderProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_PROVIDER_VALUES!r}"
    )
