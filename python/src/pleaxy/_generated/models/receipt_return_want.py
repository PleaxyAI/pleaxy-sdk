from typing import Literal, Set, cast

ReceiptReturnWant = Literal["credit_note", "none", "replacement"]

RECEIPT_RETURN_WANT_VALUES: Set[ReceiptReturnWant] = {
    "credit_note",
    "none",
    "replacement",
}


def check_receipt_return_want(value: str) -> ReceiptReturnWant:
    if value in RECEIPT_RETURN_WANT_VALUES:
        return cast(ReceiptReturnWant, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECEIPT_RETURN_WANT_VALUES!r}"
    )
