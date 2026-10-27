from typing import Literal, Set, cast

SupplierPaymentProblemViewKind = Literal["amount_differs", "not_received"]

SUPPLIER_PAYMENT_PROBLEM_VIEW_KIND_VALUES: Set[SupplierPaymentProblemViewKind] = {
    "amount_differs",
    "not_received",
}


def check_supplier_payment_problem_view_kind(
    value: str,
) -> SupplierPaymentProblemViewKind:
    if value in SUPPLIER_PAYMENT_PROBLEM_VIEW_KIND_VALUES:
        return cast(SupplierPaymentProblemViewKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_PAYMENT_PROBLEM_VIEW_KIND_VALUES!r}"
    )
