from typing import Literal, Set, cast

SelfApprovalRecordBasis = Literal["sole_eligible_approver"]

SELF_APPROVAL_RECORD_BASIS_VALUES: Set[SelfApprovalRecordBasis] = {
    "sole_eligible_approver",
}


def check_self_approval_record_basis(value: str) -> SelfApprovalRecordBasis:
    if value in SELF_APPROVAL_RECORD_BASIS_VALUES:
        return cast(SelfApprovalRecordBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SELF_APPROVAL_RECORD_BASIS_VALUES!r}"
    )
