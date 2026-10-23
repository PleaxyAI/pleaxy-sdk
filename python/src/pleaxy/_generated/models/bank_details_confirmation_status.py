from typing import Literal, Set, cast

BankDetailsConfirmationStatus = Literal["confirmed", "disputed", "pending"]

BANK_DETAILS_CONFIRMATION_STATUS_VALUES: Set[BankDetailsConfirmationStatus] = {
    "confirmed",
    "disputed",
    "pending",
}


def check_bank_details_confirmation_status(value: str) -> BankDetailsConfirmationStatus:
    if value in BANK_DETAILS_CONFIRMATION_STATUS_VALUES:
        return cast(BankDetailsConfirmationStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_DETAILS_CONFIRMATION_STATUS_VALUES!r}"
    )
