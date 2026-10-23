from typing import Literal, Set, cast

BankDetailsConfirmationDisputeReason = Literal["not_sent", "wrong_bank_details"]

BANK_DETAILS_CONFIRMATION_DISPUTE_REASON_VALUES: Set[
    BankDetailsConfirmationDisputeReason
] = {
    "not_sent",
    "wrong_bank_details",
}


def check_bank_details_confirmation_dispute_reason(
    value: str,
) -> BankDetailsConfirmationDisputeReason:
    if value in BANK_DETAILS_CONFIRMATION_DISPUTE_REASON_VALUES:
        return cast(BankDetailsConfirmationDisputeReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BANK_DETAILS_CONFIRMATION_DISPUTE_REASON_VALUES!r}"
    )
