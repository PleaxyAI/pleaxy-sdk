from typing import Literal, Set, cast

RemittanceViewPaymentMethod = Literal[
    "ach", "card", "check", "credit", "nothing_due", "other", "stripe", "wire"
]

REMITTANCE_VIEW_PAYMENT_METHOD_VALUES: Set[RemittanceViewPaymentMethod] = {
    "ach",
    "card",
    "check",
    "credit",
    "nothing_due",
    "other",
    "stripe",
    "wire",
}


def check_remittance_view_payment_method(value: str) -> RemittanceViewPaymentMethod:
    if value in REMITTANCE_VIEW_PAYMENT_METHOD_VALUES:
        return cast(RemittanceViewPaymentMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_VIEW_PAYMENT_METHOD_VALUES!r}"
    )
