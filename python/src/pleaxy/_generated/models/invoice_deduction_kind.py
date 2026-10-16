from typing import Literal, Set, cast

InvoiceDeductionKind = Literal["credit", "prepayment"]

INVOICE_DEDUCTION_KIND_VALUES: Set[InvoiceDeductionKind] = {
    "credit",
    "prepayment",
}


def check_invoice_deduction_kind(value: str) -> InvoiceDeductionKind:
    if value in INVOICE_DEDUCTION_KIND_VALUES:
        return cast(InvoiceDeductionKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_DEDUCTION_KIND_VALUES!r}"
    )
