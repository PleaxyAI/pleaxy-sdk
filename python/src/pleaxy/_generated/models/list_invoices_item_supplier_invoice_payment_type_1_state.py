from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoicePaymentType1State = Literal["processing", "succeeded"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES: Set[
    ListInvoicesItemSupplierInvoicePaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_list_invoices_item_supplier_invoice_payment_type_1_state(
    value: str,
) -> ListInvoicesItemSupplierInvoicePaymentType1State:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(ListInvoicesItemSupplierInvoicePaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
