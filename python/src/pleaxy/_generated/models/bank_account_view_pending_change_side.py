from typing import Literal, Set, cast

BankAccountViewPendingChangeSide = Literal["buyer", "supplier"]

BANK_ACCOUNT_VIEW_PENDING_CHANGE_SIDE_VALUES: Set[BankAccountViewPendingChangeSide] = {
    "buyer",
    "supplier",
}


def check_bank_account_view_pending_change_side(
    value: str,
) -> BankAccountViewPendingChangeSide:
    if value in BANK_ACCOUNT_VIEW_PENDING_CHANGE_SIDE_VALUES:
        return cast(BankAccountViewPendingChangeSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_VIEW_PENDING_CHANGE_SIDE_VALUES!r}"
    )
