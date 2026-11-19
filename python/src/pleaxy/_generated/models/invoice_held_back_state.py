from typing import Literal, Set, cast

InvoiceHeldBackState = Literal["answered", "carried", "open", "paid", "released"]

INVOICE_HELD_BACK_STATE_VALUES: Set[InvoiceHeldBackState] = {
    "answered",
    "carried",
    "open",
    "paid",
    "released",
}


def check_invoice_held_back_state(value: str) -> InvoiceHeldBackState:
    if value in INVOICE_HELD_BACK_STATE_VALUES:
        return cast(InvoiceHeldBackState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_HELD_BACK_STATE_VALUES!r}"
    )
