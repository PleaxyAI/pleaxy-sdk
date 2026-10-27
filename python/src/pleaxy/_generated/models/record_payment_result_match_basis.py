from typing import Literal, Set, cast

RecordPaymentResultMatchBasis = Literal["no_po_history", "purchase_order"]

RECORD_PAYMENT_RESULT_MATCH_BASIS_VALUES: Set[RecordPaymentResultMatchBasis] = {
    "no_po_history",
    "purchase_order",
}


def check_record_payment_result_match_basis(
    value: str,
) -> RecordPaymentResultMatchBasis:
    if value in RECORD_PAYMENT_RESULT_MATCH_BASIS_VALUES:
        return cast(RecordPaymentResultMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_MATCH_BASIS_VALUES!r}"
    )
