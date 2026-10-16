from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Method = Literal[
    "ach", "card", "check", "credit", "other", "wire"
]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "other",
    "wire",
}


def check_list_invoices_item_supplier_invoice_withdrawn_payment_type_0_method(
    value: str,
) -> ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Method:
    if (
        value
        in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES
    ):
        return cast(ListInvoicesItemSupplierInvoiceWithdrawnPaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
