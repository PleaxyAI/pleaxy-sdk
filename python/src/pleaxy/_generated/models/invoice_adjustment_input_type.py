from typing import Literal, Set, cast

InvoiceAdjustmentInputType = Literal["charge", "discount"]

INVOICE_ADJUSTMENT_INPUT_TYPE_VALUES: Set[InvoiceAdjustmentInputType] = {
    "charge",
    "discount",
}


def check_invoice_adjustment_input_type(value: str) -> InvoiceAdjustmentInputType:
    if value in INVOICE_ADJUSTMENT_INPUT_TYPE_VALUES:
        return cast(InvoiceAdjustmentInputType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_ADJUSTMENT_INPUT_TYPE_VALUES!r}"
    )
