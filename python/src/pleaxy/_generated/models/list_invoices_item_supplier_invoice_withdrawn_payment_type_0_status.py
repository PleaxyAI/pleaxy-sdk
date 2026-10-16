from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Status = Literal["recorded"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Status
] = {
    "recorded",
}


def check_list_invoices_item_supplier_invoice_withdrawn_payment_type_0_status(
    value: str,
) -> ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Status:
    if (
        value
        in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES
    ):
        return cast(ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
