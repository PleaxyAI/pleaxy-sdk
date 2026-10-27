from typing import Literal, Set, cast

InvoiceSettlementSource = Literal[
    "buyer_marked",
    "no_money_moved",
    "no_problem_reported",
    "stripe",
    "supplier_confirmed",
]

INVOICE_SETTLEMENT_SOURCE_VALUES: Set[InvoiceSettlementSource] = {
    "buyer_marked",
    "no_money_moved",
    "no_problem_reported",
    "stripe",
    "supplier_confirmed",
}


def check_invoice_settlement_source(value: str) -> InvoiceSettlementSource:
    if value in INVOICE_SETTLEMENT_SOURCE_VALUES:
        return cast(InvoiceSettlementSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SETTLEMENT_SOURCE_VALUES!r}"
    )
