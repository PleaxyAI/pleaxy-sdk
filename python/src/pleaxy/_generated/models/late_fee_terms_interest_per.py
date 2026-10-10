from typing import Literal, Set, cast

LateFeeTermsInterestPer = Literal["month", "year"]

LATE_FEE_TERMS_INTEREST_PER_VALUES: Set[LateFeeTermsInterestPer] = {
    "month",
    "year",
}


def check_late_fee_terms_interest_per(value: str) -> LateFeeTermsInterestPer:
    if value in LATE_FEE_TERMS_INTEREST_PER_VALUES:
        return cast(LateFeeTermsInterestPer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LATE_FEE_TERMS_INTEREST_PER_VALUES!r}"
    )
