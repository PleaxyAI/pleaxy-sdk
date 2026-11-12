from typing import Literal, Set, cast

InvoiceActivityEntryActorSide = Literal["buyer", "supplier", "system"]

INVOICE_ACTIVITY_ENTRY_ACTOR_SIDE_VALUES: Set[InvoiceActivityEntryActorSide] = {
    "buyer",
    "supplier",
    "system",
}


def check_invoice_activity_entry_actor_side(
    value: str,
) -> InvoiceActivityEntryActorSide:
    if value in INVOICE_ACTIVITY_ENTRY_ACTOR_SIDE_VALUES:
        return cast(InvoiceActivityEntryActorSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_ACTIVITY_ENTRY_ACTOR_SIDE_VALUES!r}"
    )
