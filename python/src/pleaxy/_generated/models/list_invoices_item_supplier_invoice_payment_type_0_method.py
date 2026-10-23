from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoicePaymentType0Method = Literal[
    "ach", "card", "check", "credit", "nothing_due", "other", "wire"
]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    ListInvoicesItemSupplierInvoicePaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "nothing_due",
    "other",
    "wire",
}


def check_list_invoices_item_supplier_invoice_payment_type_0_method(
    value: str,
) -> ListInvoicesItemSupplierInvoicePaymentType0Method:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(ListInvoicesItemSupplierInvoicePaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
