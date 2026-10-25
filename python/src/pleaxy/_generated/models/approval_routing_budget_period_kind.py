from typing import Literal, Set, cast

ApprovalRoutingBudgetPeriodKind = Literal["month", "quarter", "year"]

APPROVAL_ROUTING_BUDGET_PERIOD_KIND_VALUES: Set[ApprovalRoutingBudgetPeriodKind] = {
    "month",
    "quarter",
    "year",
}


def check_approval_routing_budget_period_kind(
    value: str,
) -> ApprovalRoutingBudgetPeriodKind:
    if value in APPROVAL_ROUTING_BUDGET_PERIOD_KIND_VALUES:
        return cast(ApprovalRoutingBudgetPeriodKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_ROUTING_BUDGET_PERIOD_KIND_VALUES!r}"
    )
