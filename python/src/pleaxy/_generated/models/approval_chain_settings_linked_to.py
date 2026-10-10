from typing import Literal, Set, cast

ApprovalChainSettingsLinkedTo = Literal["invoice_payment", "purchase_order"]

APPROVAL_CHAIN_SETTINGS_LINKED_TO_VALUES: Set[ApprovalChainSettingsLinkedTo] = {
    "invoice_payment",
    "purchase_order",
}


def check_approval_chain_settings_linked_to(
    value: str,
) -> ApprovalChainSettingsLinkedTo:
    if value in APPROVAL_CHAIN_SETTINGS_LINKED_TO_VALUES:
        return cast(ApprovalChainSettingsLinkedTo, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {APPROVAL_CHAIN_SETTINGS_LINKED_TO_VALUES!r}"
    )
