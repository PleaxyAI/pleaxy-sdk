from typing import Literal, Set, cast

ApprovalHistoryEntryAction = Literal[
    "approved", "limit_exceeded", "reassigned", "rejected", "skipped"
]

APPROVAL_HISTORY_ENTRY_ACTION_VALUES: Set[ApprovalHistoryEntryAction] = {
    "approved",
    "limit_exceeded",
    "reassigned",
    "rejected",
    "skipped",
}


def check_approval_history_entry_action(value: str) -> ApprovalHistoryEntryAction:
    if value in APPROVAL_HISTORY_ENTRY_ACTION_VALUES:
        return cast(ApprovalHistoryEntryAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_HISTORY_ENTRY_ACTION_VALUES!r}"
    )
