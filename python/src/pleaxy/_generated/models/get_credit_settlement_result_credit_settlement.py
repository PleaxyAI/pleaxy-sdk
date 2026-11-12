from typing import Literal, Set, cast

GetCreditSettlementResultCreditSettlement = Literal["accounting_system", "pleaxy"]

GET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES: Set[
    GetCreditSettlementResultCreditSettlement
] = {
    "accounting_system",
    "pleaxy",
}


def check_get_credit_settlement_result_credit_settlement(
    value: str,
) -> GetCreditSettlementResultCreditSettlement:
    if value in GET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES:
        return cast(GetCreditSettlementResultCreditSettlement, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CREDIT_SETTLEMENT_RESULT_CREDIT_SETTLEMENT_VALUES!r}"
    )
