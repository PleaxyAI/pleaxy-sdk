from typing import Literal, Set, cast

ApprovalRoutingTouchlessSkipped = Literal["human_only", "other_currency"]

APPROVAL_ROUTING_TOUCHLESS_SKIPPED_VALUES: Set[ApprovalRoutingTouchlessSkipped] = {
    "human_only",
    "other_currency",
}


def check_approval_routing_touchless_skipped(
    value: str,
) -> ApprovalRoutingTouchlessSkipped:
    if value in APPROVAL_ROUTING_TOUCHLESS_SKIPPED_VALUES:
        return cast(ApprovalRoutingTouchlessSkipped, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_ROUTING_TOUCHLESS_SKIPPED_VALUES!r}"
    )
