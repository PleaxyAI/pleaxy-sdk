from typing import Literal, Set, cast

CreditSettlementInputCreditSettlement = Literal["accounting_system", "pleaxy"]

CREDIT_SETTLEMENT_INPUT_CREDIT_SETTLEMENT_VALUES: Set[
    CreditSettlementInputCreditSettlement
] = {
    "accounting_system",
    "pleaxy",
}


def check_credit_settlement_input_credit_settlement(
    value: str,
) -> CreditSettlementInputCreditSettlement:
    if value in CREDIT_SETTLEMENT_INPUT_CREDIT_SETTLEMENT_VALUES:
        return cast(CreditSettlementInputCreditSettlement, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_SETTLEMENT_INPUT_CREDIT_SETTLEMENT_VALUES!r}"
    )
