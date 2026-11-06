from typing import Literal, Set, cast

BillingSummaryModulesItem = Literal[
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

BILLING_SUMMARY_MODULES_ITEM_VALUES: Set[BillingSummaryModulesItem] = {
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


def check_billing_summary_modules_item(value: str) -> BillingSummaryModulesItem:
    if value in BILLING_SUMMARY_MODULES_ITEM_VALUES:
        return cast(BillingSummaryModulesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_MODULES_ITEM_VALUES!r}"
    )
