from typing import Literal, Set, cast

EInvoiceVatCategory = Literal["AE", "E", "G", "K", "L", "M", "O", "S", "Z"]

E_INVOICE_VAT_CATEGORY_VALUES: Set[EInvoiceVatCategory] = {
    "AE",
    "E",
    "G",
    "K",
    "L",
    "M",
    "O",
    "S",
    "Z",
}


def check_e_invoice_vat_category(value: str) -> EInvoiceVatCategory:
    if value in E_INVOICE_VAT_CATEGORY_VALUES:
        return cast(EInvoiceVatCategory, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_VAT_CATEGORY_VALUES!r}"
    )
