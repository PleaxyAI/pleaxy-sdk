from typing import Literal, Set, cast

ApprovalRoutingBudgetOutcome = Literal["no_budget", "no_rate", "off", "over", "within"]

APPROVAL_ROUTING_BUDGET_OUTCOME_VALUES: Set[ApprovalRoutingBudgetOutcome] = {
    "no_budget",
    "no_rate",
    "off",
    "over",
    "within",
}


def check_approval_routing_budget_outcome(value: str) -> ApprovalRoutingBudgetOutcome:
    if value in APPROVAL_ROUTING_BUDGET_OUTCOME_VALUES:
        return cast(ApprovalRoutingBudgetOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_ROUTING_BUDGET_OUTCOME_VALUES!r}"
    )
