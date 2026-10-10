from typing import Literal, Set, cast

SelfApprovalRecordWaivedExclusion = Literal[
    "entered this invoice", "over their own spend limit", "spend-limit review"
]

SELF_APPROVAL_RECORD_WAIVED_EXCLUSION_VALUES: Set[SelfApprovalRecordWaivedExclusion] = {
    "entered this invoice",
    "over their own spend limit",
    "spend-limit review",
}


def check_self_approval_record_waived_exclusion(
    value: str,
) -> SelfApprovalRecordWaivedExclusion:
    if value in SELF_APPROVAL_RECORD_WAIVED_EXCLUSION_VALUES:
        return cast(SelfApprovalRecordWaivedExclusion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SELF_APPROVAL_RECORD_WAIVED_EXCLUSION_VALUES!r}"
    )
