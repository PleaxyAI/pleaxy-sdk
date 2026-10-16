from typing import Literal, Set, cast

PurchaseOrderSupplierViewPriorInvoicedBasis = Literal["invoiced", "remaining"]

PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_BASIS_VALUES: Set[
    PurchaseOrderSupplierViewPriorInvoicedBasis
] = {
    "invoiced",
    "remaining",
}


def check_purchase_order_supplier_view_prior_invoiced_basis(
    value: str,
) -> PurchaseOrderSupplierViewPriorInvoicedBasis:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_BASIS_VALUES:
        return cast(PurchaseOrderSupplierViewPriorInvoicedBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_BASIS_VALUES!r}"
    )
