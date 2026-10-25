from typing import Literal, Set, cast

InvoiceAccessRemovalAction = Literal["removed", "role_changed"]

INVOICE_ACCESS_REMOVAL_ACTION_VALUES: Set[InvoiceAccessRemovalAction] = {
    "removed",
    "role_changed",
}


def check_invoice_access_removal_action(value: str) -> InvoiceAccessRemovalAction:
    if value in INVOICE_ACCESS_REMOVAL_ACTION_VALUES:
        return cast(InvoiceAccessRemovalAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_ACCESS_REMOVAL_ACTION_VALUES!r}"
    )
