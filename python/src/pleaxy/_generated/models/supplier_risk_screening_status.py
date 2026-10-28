from typing import Literal, Set, cast

SupplierRiskScreeningStatus = Literal[
    "clear", "confirmed_match", "not_screened", "off", "possible_match"
]

SUPPLIER_RISK_SCREENING_STATUS_VALUES: Set[SupplierRiskScreeningStatus] = {
    "clear",
    "confirmed_match",
    "not_screened",
    "off",
    "possible_match",
}


def check_supplier_risk_screening_status(value: str) -> SupplierRiskScreeningStatus:
    if value in SUPPLIER_RISK_SCREENING_STATUS_VALUES:
        return cast(SupplierRiskScreeningStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_SCREENING_STATUS_VALUES!r}"
    )
