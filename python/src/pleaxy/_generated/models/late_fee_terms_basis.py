from typing import Literal, Set, cast

LateFeeTermsBasis = Literal["contractual", "statutory"]

LATE_FEE_TERMS_BASIS_VALUES: Set[LateFeeTermsBasis] = {
    "contractual",
    "statutory",
}


def check_late_fee_terms_basis(value: str) -> LateFeeTermsBasis:
    if value in LATE_FEE_TERMS_BASIS_VALUES:
        return cast(LateFeeTermsBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LATE_FEE_TERMS_BASIS_VALUES!r}"
    )
