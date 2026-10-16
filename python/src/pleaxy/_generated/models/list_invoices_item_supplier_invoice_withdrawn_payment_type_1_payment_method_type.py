from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_list_invoices_item_supplier_invoice_withdrawn_payment_type_1_payment_method_type(
    value: str,
) -> ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1PaymentMethodType:
    if (
        value
        in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(
            ListInvoicesItemSupplierInvoiceWithdrawnPaymentType1PaymentMethodType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
