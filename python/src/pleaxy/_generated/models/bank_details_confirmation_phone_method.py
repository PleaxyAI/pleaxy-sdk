from typing import Literal, Set, cast

BankDetailsConfirmationPhoneMethod = Literal["callback", "letter", "other"]

BANK_DETAILS_CONFIRMATION_PHONE_METHOD_VALUES: Set[
    BankDetailsConfirmationPhoneMethod
] = {
    "callback",
    "letter",
    "other",
}


def check_bank_details_confirmation_phone_method(
    value: str,
) -> BankDetailsConfirmationPhoneMethod:
    if value in BANK_DETAILS_CONFIRMATION_PHONE_METHOD_VALUES:
        return cast(BankDetailsConfirmationPhoneMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_DETAILS_CONFIRMATION_PHONE_METHOD_VALUES!r}"
    )
