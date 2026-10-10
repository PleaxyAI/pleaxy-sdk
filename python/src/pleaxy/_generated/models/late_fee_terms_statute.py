from typing import Literal, Set, cast

LateFeeTermsStatute = Literal["eu_late_payment_directive", "uk_late_payment_act"]

LATE_FEE_TERMS_STATUTE_VALUES: Set[LateFeeTermsStatute] = {
    "eu_late_payment_directive",
    "uk_late_payment_act",
}


def check_late_fee_terms_statute(value: str) -> LateFeeTermsStatute:
    if value in LATE_FEE_TERMS_STATUTE_VALUES:
        return cast(LateFeeTermsStatute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LATE_FEE_TERMS_STATUTE_VALUES!r}"
    )
