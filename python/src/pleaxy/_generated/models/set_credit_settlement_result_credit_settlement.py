from typing import Literal, Set, cast

SetCreditSettlementResultCreditSettlement = Literal["accounting_system", "pleaxy"]

SET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES: Set[
    SetCreditSettlementResultCreditSettlement
] = {
    "accounting_system",
    "pleaxy",
}


def check_set_credit_settlement_result_credit_settlement(
    value: str,
) -> SetCreditSettlementResultCreditSettlement:
    if value in SET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES:
        return cast(SetCreditSettlementResultCreditSettlement, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES!r}"
    )
