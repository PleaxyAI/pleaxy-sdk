from typing import Literal, Set, cast

PurchaseOrderChangeSummaryOutcome = Literal["approved", "draft", "reapproval"]

PURCHASE_ORDER_CHANGE_SUMMARY_OUTCOME_VALUES: Set[PurchaseOrderChangeSummaryOutcome] = {
    "approved",
    "draft",
    "reapproval",
}


def check_purchase_order_change_summary_outcome(
    value: str,
) -> PurchaseOrderChangeSummaryOutcome:
    if value in PURCHASE_ORDER_CHANGE_SUMMARY_OUTCOME_VALUES:
        return cast(PurchaseOrderChangeSummaryOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_CHANGE_SUMMARY_OUTCOME_VALUES!r}"
    )
