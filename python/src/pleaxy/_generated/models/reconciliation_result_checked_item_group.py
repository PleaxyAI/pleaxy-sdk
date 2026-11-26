from typing import Literal, Set, cast

ReconciliationResultCheckedItemGroup = Literal["agreement", "order", "receipt", "usage"]

RECONCILIATION_RESULT_CHECKED_ITEM_GROUP_VALUES: Set[
    ReconciliationResultCheckedItemGroup
] = {
    "agreement",
    "order",
    "receipt",
    "usage",
}


def check_reconciliation_result_checked_item_group(
    value: str,
) -> ReconciliationResultCheckedItemGroup:
    if value in RECONCILIATION_RESULT_CHECKED_ITEM_GROUP_VALUES:
        return cast(ReconciliationResultCheckedItemGroup, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_CHECKED_ITEM_GROUP_VALUES!r}"
    )
