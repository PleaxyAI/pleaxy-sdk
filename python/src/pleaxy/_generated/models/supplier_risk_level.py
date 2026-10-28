from typing import Literal, Set, cast

SupplierRiskLevel = Literal["attention", "blocked", "ok"]

SUPPLIER_RISK_LEVEL_VALUES: Set[SupplierRiskLevel] = {
    "attention",
    "blocked",
    "ok",
}


def check_supplier_risk_level(value: str) -> SupplierRiskLevel:
    if value in SUPPLIER_RISK_LEVEL_VALUES:
        return cast(SupplierRiskLevel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_LEVEL_VALUES!r}"
    )
