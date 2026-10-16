from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoicePaymentType1Status = Literal["stripe"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    ListInvoicesItemSupplierInvoicePaymentType1Status
] = {
    "stripe",
}


def check_list_invoices_item_supplier_invoice_payment_type_1_status(
    value: str,
) -> ListInvoicesItemSupplierInvoicePaymentType1Status:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(ListInvoicesItemSupplierInvoicePaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
