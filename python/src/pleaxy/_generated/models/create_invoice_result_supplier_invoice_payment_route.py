from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentRoute = Literal["erp", "pleaxy"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_create_invoice_result_supplier_invoice_payment_route(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentRoute:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(CreateInvoiceResultSupplierInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
