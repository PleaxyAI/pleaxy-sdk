from typing import Literal, Set, cast

PurchaseOrderSupplierViewPriorInvoicedSourceSystem = Literal[
    "coupa", "oracle", "sap_ariba"
]

PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES: Set[
    PurchaseOrderSupplierViewPriorInvoicedSourceSystem
] = {
    "coupa",
    "oracle",
    "sap_ariba",
}


def check_purchase_order_supplier_view_prior_invoiced_source_system(
    value: str,
) -> PurchaseOrderSupplierViewPriorInvoicedSourceSystem:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES:
        return cast(PurchaseOrderSupplierViewPriorInvoicedSourceSystem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_PRIOR_INVOICED_SOURCE_SYSTEM_VALUES!r}"
    )
