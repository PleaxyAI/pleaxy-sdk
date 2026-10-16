from typing import Literal, Set, cast

InvoiceDeductionInputKind = Literal["credit", "prepayment"]

INVOICE_DEDUCTION_INPUT_KIND_VALUES: Set[InvoiceDeductionInputKind] = {
    "credit",
    "prepayment",
}


def check_invoice_deduction_input_kind(value: str) -> InvoiceDeductionInputKind:
    if value in INVOICE_DEDUCTION_INPUT_KIND_VALUES:
        return cast(InvoiceDeductionInputKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_DEDUCTION_INPUT_KIND_VALUES!r}"
    )
