from typing import Literal, Set, cast

BillingSummaryPendingModuleRemovalModulesItem = Literal[
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "receipt",
    "request",
    "sourcing",
    "suppliers",
]

BILLING_SUMMARY_PENDING_MODULE_REMOVAL_MODULES_ITEM_VALUES: Set[
    BillingSummaryPendingModuleRemovalModulesItem
] = {
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "receipt",
    "request",
    "sourcing",
    "suppliers",
}


def check_billing_summary_pending_module_removal_modules_item(
    value: str,
) -> BillingSummaryPendingModuleRemovalModulesItem:
    if value in BILLING_SUMMARY_PENDING_MODULE_REMOVAL_MODULES_ITEM_VALUES:
        return cast(BillingSummaryPendingModuleRemovalModulesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_PENDING_MODULE_REMOVAL_MODULES_ITEM_VALUES!r}"
    )
