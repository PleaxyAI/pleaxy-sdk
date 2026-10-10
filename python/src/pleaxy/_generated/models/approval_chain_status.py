from typing import Literal, Set, cast

ApprovalChainStatus = Literal["approved", "pending", "rejected"]

APPROVAL_CHAIN_STATUS_VALUES: Set[ApprovalChainStatus] = {
    "approved",
    "pending",
    "rejected",
}


def check_approval_chain_status(value: str) -> ApprovalChainStatus:
    if value in APPROVAL_CHAIN_STATUS_VALUES:
        return cast(ApprovalChainStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_CHAIN_STATUS_VALUES!r}"
    )
