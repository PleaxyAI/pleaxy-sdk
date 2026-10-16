from typing import Literal, Set, cast

PurchaseOrderPriorInvoicedSourceSystem = Literal["coupa", "oracle", "sap_ariba"]

PURCHASE_ORDER_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES: Set[
    PurchaseOrderPriorInvoicedSourceSystem
] = {
    "coupa",
    "oracle",
    "sap_ariba",
}


def check_purchase_order_prior_invoiced_source_system(
    value: str,
) -> PurchaseOrderPriorInvoicedSourceSystem:
    if value in PURCHASE_ORDER_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES:
        return cast(PurchaseOrderPriorInvoicedSourceSystem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES!r}"
    )
