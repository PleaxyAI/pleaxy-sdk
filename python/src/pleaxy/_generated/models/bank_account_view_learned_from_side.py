from typing import Literal, Set, cast

BankAccountViewLearnedFromSide = Literal["buyer", "supplier"]

BANK_ACCOUNT_VIEW_LEARNED_FROM_SIDE_VALUES: Set[BankAccountViewLearnedFromSide] = {
    "buyer",
    "supplier",
}


def check_bank_account_view_learned_from_side(
    value: str,
) -> BankAccountViewLearnedFromSide:
    if value in BANK_ACCOUNT_VIEW_LEARNED_FROM_SIDE_VALUES:
        return cast(BankAccountViewLearnedFromSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_VIEW_LEARNED_FROM_SIDE_VALUES!r}"
    )
