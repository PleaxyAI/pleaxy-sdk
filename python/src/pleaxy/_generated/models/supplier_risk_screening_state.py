from typing import Literal, Set, cast

SupplierRiskScreeningState = Literal["attention", "blocked", "none", "ok"]

SUPPLIER_RISK_SCREENING_STATE_VALUES: Set[SupplierRiskScreeningState] = {
    "attention",
    "blocked",
    "none",
    "ok",
}


def check_supplier_risk_screening_state(value: str) -> SupplierRiskScreeningState:
    if value in SUPPLIER_RISK_SCREENING_STATE_VALUES:
        return cast(SupplierRiskScreeningState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_SCREENING_STATE_VALUES!r}"
    )
