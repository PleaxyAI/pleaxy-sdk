from typing import Literal, Set, cast

SupplierRiskBankState = Literal["attention", "blocked", "none", "ok"]

SUPPLIER_RISK_BANK_STATE_VALUES: Set[SupplierRiskBankState] = {
    "attention",
    "blocked",
    "none",
    "ok",
}


def check_supplier_risk_bank_state(value: str) -> SupplierRiskBankState:
    if value in SUPPLIER_RISK_BANK_STATE_VALUES:
        return cast(SupplierRiskBankState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_BANK_STATE_VALUES!r}"
    )
