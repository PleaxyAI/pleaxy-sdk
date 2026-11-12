from typing import Literal, Set, cast

ListAvailableCreditsResultCreditSettlement = Literal["accounting_system", "pleaxy"]

LIST_AVAILABLE_CREDITS_RESULT_CREDIT_SETTLEMENT_VALUES: Set[
    ListAvailableCreditsResultCreditSettlement
] = {
    "accounting_system",
    "pleaxy",
}


def check_list_available_credits_result_credit_settlement(
    value: str,
) -> ListAvailableCreditsResultCreditSettlement:
    if value in LIST_AVAILABLE_CREDITS_RESULT_CREDIT_SETTLEMENT_VALUES:
        return cast(ListAvailableCreditsResultCreditSettlement, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AVAILABLE_CREDITS_RESULT_CREDIT_SETTLEMENT_VALUES!r}"
    )
