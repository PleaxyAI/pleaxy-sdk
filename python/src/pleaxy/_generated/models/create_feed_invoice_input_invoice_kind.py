from typing import Literal, Set, cast

CreateFeedInvoiceInputInvoiceKind = Literal["prepayment"]

CREATE_FEED_INVOICE_INPUT_INVOICE_KIND_VALUES: Set[
    CreateFeedInvoiceInputInvoiceKind
] = {
    "prepayment",
}


def check_create_feed_invoice_input_invoice_kind(
    value: str,
) -> CreateFeedInvoiceInputInvoiceKind:
    if value in CREATE_FEED_INVOICE_INPUT_INVOICE_KIND_VALUES:
        return cast(CreateFeedInvoiceInputInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_FEED_INVOICE_INPUT_INVOICE_KIND_VALUES!r}"
    )
