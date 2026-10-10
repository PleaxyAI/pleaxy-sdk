from typing import Literal, Set, cast

UpdateApprovalChainInputLinkedTo = Literal["invoice_payment", "purchase_order"]

UPDATE_APPROVAL_CHAIN_INPUT_LINKED_TO_VALUES: Set[UpdateApprovalChainInputLinkedTo] = {
    "invoice_payment",
    "purchase_order",
}


def check_update_approval_chain_input_linked_to(
    value: str,
) -> UpdateApprovalChainInputLinkedTo:
    if value in UPDATE_APPROVAL_CHAIN_INPUT_LINKED_TO_VALUES:
        return cast(UpdateApprovalChainInputLinkedTo, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_APPROVAL_CHAIN_INPUT_LINKED_TO_VALUES!r}"
    )
