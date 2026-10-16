from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceSubmittedFormat = Literal["cxml", "json", "ubl"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    ListInvoicesItemSupplierInvoiceSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_list_invoices_item_supplier_invoice_submitted_format(
    value: str,
) -> ListInvoicesItemSupplierInvoiceSubmittedFormat:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
