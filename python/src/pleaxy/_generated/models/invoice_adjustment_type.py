from typing import Literal, Set, cast

InvoiceAdjustmentType = Literal["charge", "discount"]

INVOICE_ADJUSTMENT_TYPE_VALUES: Set[InvoiceAdjustmentType] = {
    "charge",
    "discount",
}


def check_invoice_adjustment_type(value: str) -> InvoiceAdjustmentType:
    if value in INVOICE_ADJUSTMENT_TYPE_VALUES:
        return cast(InvoiceAdjustmentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_ADJUSTMENT_TYPE_VALUES!r}"
    )
