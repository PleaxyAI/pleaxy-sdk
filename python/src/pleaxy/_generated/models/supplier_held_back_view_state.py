from typing import Literal, Set, cast

SupplierHeldBackViewState = Literal["answered", "carried", "open", "paid", "released"]

SUPPLIER_HELD_BACK_VIEW_STATE_VALUES: Set[SupplierHeldBackViewState] = {
    "answered",
    "carried",
    "open",
    "paid",
    "released",
}


def check_supplier_held_back_view_state(value: str) -> SupplierHeldBackViewState:
    if value in SUPPLIER_HELD_BACK_VIEW_STATE_VALUES:
        return cast(SupplierHeldBackViewState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_HELD_BACK_VIEW_STATE_VALUES!r}"
    )
