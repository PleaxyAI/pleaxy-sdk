from typing import Literal, Set, cast

ApprovalReassignmentDetailOnRebuild = Literal["carried", "not-carried"]

APPROVAL_REASSIGNMENT_DETAIL_ON_REBUILD_VALUES: Set[
    ApprovalReassignmentDetailOnRebuild
] = {
    "carried",
    "not-carried",
}


def check_approval_reassignment_detail_on_rebuild(
    value: str,
) -> ApprovalReassignmentDetailOnRebuild:
    if value in APPROVAL_REASSIGNMENT_DETAIL_ON_REBUILD_VALUES:
        return cast(ApprovalReassignmentDetailOnRebuild, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_REASSIGNMENT_DETAIL_ON_REBUILD_VALUES!r}"
    )
