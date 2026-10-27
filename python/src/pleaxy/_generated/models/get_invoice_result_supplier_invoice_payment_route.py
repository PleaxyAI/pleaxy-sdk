from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentRoute = Literal["erp", "pleaxy"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_get_invoice_result_supplier_invoice_payment_route(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentRoute:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES:
        return cast(GetInvoiceResultSupplierInvoicePaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_ROUTE_VALUES!r}"
    )
