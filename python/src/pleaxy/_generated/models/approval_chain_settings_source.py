from typing import Literal, Set, cast

ApprovalChainSettingsSource = Literal["default"]

APPROVAL_CHAIN_SETTINGS_SOURCE_VALUES: Set[ApprovalChainSettingsSource] = {
    "default",
}


def check_approval_chain_settings_source(value: str) -> ApprovalChainSettingsSource:
    if value in APPROVAL_CHAIN_SETTINGS_SOURCE_VALUES:
        return cast(ApprovalChainSettingsSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_CHAIN_SETTINGS_SOURCE_VALUES!r}"
    )
