from typing import Literal, Set, cast

ApprovalHistoryEntrySkipRule = Literal["requester_in_parallel_group"]

APPROVAL_HISTORY_ENTRY_SKIP_RULE_VALUES: Set[ApprovalHistoryEntrySkipRule] = {
    "requester_in_parallel_group",
}


def check_approval_history_entry_skip_rule(value: str) -> ApprovalHistoryEntrySkipRule:
    if value in APPROVAL_HISTORY_ENTRY_SKIP_RULE_VALUES:
        return cast(ApprovalHistoryEntrySkipRule, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_HISTORY_ENTRY_SKIP_RULE_VALUES!r}"
    )
