from typing import Literal, Set, cast

SupplierScreeningHistoryItemEvent = Literal[
    "closed", "confirmed", "dismissed", "reopened", "screened"
]

SUPPLIER_SCREENING_HISTORY_ITEM_EVENT_VALUES: Set[SupplierScreeningHistoryItemEvent] = {
    "closed",
    "confirmed",
    "dismissed",
    "reopened",
    "screened",
}


def check_supplier_screening_history_item_event(
    value: str,
) -> SupplierScreeningHistoryItemEvent:
    if value in SUPPLIER_SCREENING_HISTORY_ITEM_EVENT_VALUES:
        return cast(SupplierScreeningHistoryItemEvent, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_SCREENING_HISTORY_ITEM_EVENT_VALUES!r}"
    )
