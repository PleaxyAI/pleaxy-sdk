from typing import Literal, Set, cast

SupplierSettlementViewSource = Literal[
    "buyer_marked",
    "no_money_moved",
    "no_problem_reported",
    "stripe",
    "supplier_confirmed",
]

SUPPLIER_SETTLEMENT_VIEW_SOURCE_VALUES: Set[SupplierSettlementViewSource] = {
    "buyer_marked",
    "no_money_moved",
    "no_problem_reported",
    "stripe",
    "supplier_confirmed",
}


def check_supplier_settlement_view_source(value: str) -> SupplierSettlementViewSource:
    if value in SUPPLIER_SETTLEMENT_VIEW_SOURCE_VALUES:
        return cast(SupplierSettlementViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_SETTLEMENT_VIEW_SOURCE_VALUES!r}"
    )
