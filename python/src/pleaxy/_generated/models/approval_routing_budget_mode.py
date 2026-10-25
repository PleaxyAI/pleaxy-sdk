from typing import Literal, Set, cast

ApprovalRoutingBudgetMode = Literal["block", "off", "warn"]

APPROVAL_ROUTING_BUDGET_MODE_VALUES: Set[ApprovalRoutingBudgetMode] = {
    "block",
    "off",
    "warn",
}


def check_approval_routing_budget_mode(value: str) -> ApprovalRoutingBudgetMode:
    if value in APPROVAL_ROUTING_BUDGET_MODE_VALUES:
        return cast(ApprovalRoutingBudgetMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_ROUTING_BUDGET_MODE_VALUES!r}"
    )
