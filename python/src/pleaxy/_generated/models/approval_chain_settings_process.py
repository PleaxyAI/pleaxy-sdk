from typing import Literal, Set, cast

ApprovalChainSettingsProcess = Literal[
    "invoice_payment", "purchase_order", "service_entry_sheet"
]

APPROVAL_CHAIN_SETTINGS_PROCESS_VALUES: Set[ApprovalChainSettingsProcess] = {
    "invoice_payment",
    "purchase_order",
    "service_entry_sheet",
}


def check_approval_chain_settings_process(value: str) -> ApprovalChainSettingsProcess:
    if value in APPROVAL_CHAIN_SETTINGS_PROCESS_VALUES:
        return cast(ApprovalChainSettingsProcess, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_CHAIN_SETTINGS_PROCESS_VALUES!r}"
    )
