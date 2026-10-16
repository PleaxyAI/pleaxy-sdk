from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1Status = Literal["stripe"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1Status
] = {
    "stripe",
}


def check_list_invoices_item_supplier_invoice_withdrawn_payment_type_1_status(
    value: str,
) -> ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1Status:
    if (
        value
        in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES
    ):
        return cast(ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
