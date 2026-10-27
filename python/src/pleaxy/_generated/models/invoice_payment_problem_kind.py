from typing import Literal, Set, cast

InvoicePaymentProblemKind = Literal["amount_differs", "not_received"]

INVOICE_PAYMENT_PROBLEM_KIND_VALUES: Set[InvoicePaymentProblemKind] = {
    "amount_differs",
    "not_received",
}


def check_invoice_payment_problem_kind(value: str) -> InvoicePaymentProblemKind:
    if value in INVOICE_PAYMENT_PROBLEM_KIND_VALUES:
        return cast(InvoicePaymentProblemKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_PROBLEM_KIND_VALUES!r}"
    )
