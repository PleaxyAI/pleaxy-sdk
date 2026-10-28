from typing import Literal, Set, cast

SupplierScreeningStatus = Literal[
    "clear", "confirmed_match", "not_screened", "possible_match"
]

SUPPLIER_SCREENING_STATUS_VALUES: Set[SupplierScreeningStatus] = {
    "clear",
    "confirmed_match",
    "not_screened",
    "possible_match",
}


def check_supplier_screening_status(value: str) -> SupplierScreeningStatus:
    if value in SUPPLIER_SCREENING_STATUS_VALUES:
        return cast(SupplierScreeningStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_SCREENING_STATUS_VALUES!r}"
    )
