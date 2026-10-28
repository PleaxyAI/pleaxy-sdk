from typing import Literal, Set, cast

SupplierRiskBankStatus = Literal["approved", "changing", "none", "waiting"]

SUPPLIER_RISK_BANK_STATUS_VALUES: Set[SupplierRiskBankStatus] = {
    "approved",
    "changing",
    "none",
    "waiting",
}


def check_supplier_risk_bank_status(value: str) -> SupplierRiskBankStatus:
    if value in SUPPLIER_RISK_BANK_STATUS_VALUES:
        return cast(SupplierRiskBankStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_BANK_STATUS_VALUES!r}"
    )
