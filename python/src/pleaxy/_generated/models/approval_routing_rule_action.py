from typing import Literal, Set, cast

ApprovalRoutingRuleAction = Literal["auto_approve", "require_approval"]

APPROVAL_ROUTING_RULE_ACTION_VALUES: Set[ApprovalRoutingRuleAction] = {
    "auto_approve",
    "require_approval",
}


def check_approval_routing_rule_action(value: str) -> ApprovalRoutingRuleAction:
    if value in APPROVAL_ROUTING_RULE_ACTION_VALUES:
        return cast(ApprovalRoutingRuleAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_ROUTING_RULE_ACTION_VALUES!r}"
    )
