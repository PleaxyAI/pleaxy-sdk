from typing import Literal, Set, cast

ApprovalFxSource = Literal["none", "override", "provider"]

APPROVAL_FX_SOURCE_VALUES: Set[ApprovalFxSource] = {
    "none",
    "override",
    "provider",
}


def check_approval_fx_source(value: str) -> ApprovalFxSource:
    if value in APPROVAL_FX_SOURCE_VALUES:
        return cast(ApprovalFxSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_FX_SOURCE_VALUES!r}"
    )
