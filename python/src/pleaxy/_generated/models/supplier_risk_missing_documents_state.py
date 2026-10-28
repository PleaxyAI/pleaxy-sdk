from typing import Literal, Set, cast

SupplierRiskMissingDocumentsState = Literal["attention", "blocked", "none", "ok"]

SUPPLIER_RISK_MISSING_DOCUMENTS_STATE_VALUES: Set[SupplierRiskMissingDocumentsState] = {
    "attention",
    "blocked",
    "none",
    "ok",
}


def check_supplier_risk_missing_documents_state(
    value: str,
) -> SupplierRiskMissingDocumentsState:
    if value in SUPPLIER_RISK_MISSING_DOCUMENTS_STATE_VALUES:
        return cast(SupplierRiskMissingDocumentsState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_MISSING_DOCUMENTS_STATE_VALUES!r}"
    )
