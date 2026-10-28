from typing import Literal, Set, cast

BankAccountViewStatus = Literal["changing", "unverified", "verified"]

BANK_ACCOUNT_VIEW_STATUS_VALUES: Set[BankAccountViewStatus] = {
    "changing",
    "unverified",
    "verified",
}


def check_bank_account_view_status(value: str) -> BankAccountViewStatus:
    if value in BANK_ACCOUNT_VIEW_STATUS_VALUES:
        return cast(BankAccountViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_ACCOUNT_VIEW_STATUS_VALUES!r}"
    )
