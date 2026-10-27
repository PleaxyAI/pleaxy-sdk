from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultPaymentRoute = Literal["erp", "pleaxy"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_PAYMENT_ROUTE_VALUES: Set[
    AddInvoiceReplacementLinksResultPaymentRoute
] = {
    "erp",
    "pleaxy",
}


def check_add_invoice_replacement_links_result_payment_route(
    value: str,
) -> AddInvoiceReplacementLinksResultPaymentRoute:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_PAYMENT_ROUTE_VALUES:
        return cast(AddInvoiceReplacementLinksResultPaymentRoute, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_PAYMENT_ROUTE_VALUES!r}"
    )
