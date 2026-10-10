from typing import Literal, Set, cast

PurchaseOrderSupplierViewProvider = Literal["aws", "azure", "gcp", "oci"]

PURCHASE_ORDER_SUPPLIER_VIEW_PROVIDER_VALUES: Set[PurchaseOrderSupplierViewProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_purchase_order_supplier_view_provider(
    value: str,
) -> PurchaseOrderSupplierViewProvider:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_PROVIDER_VALUES:
        return cast(PurchaseOrderSupplierViewProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_PROVIDER_VALUES!r}"
    )
