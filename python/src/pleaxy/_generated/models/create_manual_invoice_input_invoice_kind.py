from typing import Literal, Set, cast

CreateManualInvoiceInputInvoiceKind = Literal["prepayment"]

CREATE_MANUAL_INVOICE_INPUT_INVOICE_KIND_VALUES: Set[
    CreateManualInvoiceInputInvoiceKind
] = {
    "prepayment",
}


def check_create_manual_invoice_input_invoice_kind(
    value: str,
) -> CreateManualInvoiceInputInvoiceKind:
    if value in CREATE_MANUAL_INVOICE_INPUT_INVOICE_KIND_VALUES:
        return cast(CreateManualInvoiceInputInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MANUAL_INVOICE_INPUT_INVOICE_KIND_VALUES!r}"
    )
