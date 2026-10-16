from typing import Literal, Set, cast

PurchaseOrderPriorInvoicedBasis = Literal["invoiced", "remaining"]

PURCHASE_ORDER_PRIOR_INVOICED_BASIS_VALUES: Set[PurchaseOrderPriorInvoicedBasis] = {
    "invoiced",
    "remaining",
}


def check_purchase_order_prior_invoiced_basis(
    value: str,
) -> PurchaseOrderPriorInvoicedBasis:
    if value in PURCHASE_ORDER_PRIOR_INVOICED_BASIS_VALUES:
        return cast(PurchaseOrderPriorInvoicedBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_PRIOR_INVOICED_BASIS_VALUES!r}"
    )
