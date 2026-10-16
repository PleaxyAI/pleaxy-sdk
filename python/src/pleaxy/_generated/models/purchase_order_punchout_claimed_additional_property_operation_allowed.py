from typing import Literal, Set, cast

PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed = Literal[
    "create", "edit", "inspect"
]

PURCHASE_ORDER_PUNCHOUT_CLAIMED_ADDITIONAL_PROPERTY_OPERATION_ALLOWED_VALUES: Set[
    PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed
] = {
    "create",
    "edit",
    "inspect",
}


def check_purchase_order_punchout_claimed_additional_property_operation_allowed(
    value: str,
) -> PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed:
    if (
        value
        in PURCHASE_ORDER_PUNCHOUT_CLAIMED_ADDITIONAL_PROPERTY_OPERATION_ALLOWED_VALUES
    ):
        return cast(
            PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_PUNCHOUT_CLAIMED_ADDITIONAL_PROPERTY_OPERATION_ALLOWED_VALUES!r}"
    )
