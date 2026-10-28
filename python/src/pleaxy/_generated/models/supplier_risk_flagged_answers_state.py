from typing import Literal, Set, cast

SupplierRiskFlaggedAnswersState = Literal["attention", "blocked", "none", "ok"]

SUPPLIER_RISK_FLAGGED_ANSWERS_STATE_VALUES: Set[SupplierRiskFlaggedAnswersState] = {
    "attention",
    "blocked",
    "none",
    "ok",
}


def check_supplier_risk_flagged_answers_state(
    value: str,
) -> SupplierRiskFlaggedAnswersState:
    if value in SUPPLIER_RISK_FLAGGED_ANSWERS_STATE_VALUES:
        return cast(SupplierRiskFlaggedAnswersState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_RISK_FLAGGED_ANSWERS_STATE_VALUES!r}"
    )
