from typing import Literal, Set, cast

BankDetailsConfirmationConfirmedVia = Literal["phone", "supplier"]

BANK_DETAILS_CONFIRMATION_CONFIRMED_VIA_VALUES: Set[
    BankDetailsConfirmationConfirmedVia
] = {
    "phone",
    "supplier",
}


def check_bank_details_confirmation_confirmed_via(
    value: str,
) -> BankDetailsConfirmationConfirmedVia:
    if value in BANK_DETAILS_CONFIRMATION_CONFIRMED_VIA_VALUES:
        return cast(BankDetailsConfirmationConfirmedVia, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_DETAILS_CONFIRMATION_CONFIRMED_VIA_VALUES!r}"
    )
