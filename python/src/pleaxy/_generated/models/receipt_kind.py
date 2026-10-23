from typing import Literal, Set, cast

ReceiptKind = Literal["goods_receipt", "service_entry_sheet"]

RECEIPT_KIND_VALUES: Set[ReceiptKind] = {
    "goods_receipt",
    "service_entry_sheet",
}


def check_receipt_kind(value: str) -> ReceiptKind:
    if value in RECEIPT_KIND_VALUES:
        return cast(ReceiptKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECEIPT_KIND_VALUES!r}"
    )
