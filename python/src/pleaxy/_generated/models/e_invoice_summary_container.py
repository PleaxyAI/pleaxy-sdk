from typing import Literal, Set, cast

EInvoiceSummaryContainer = Literal["pdf"]

E_INVOICE_SUMMARY_CONTAINER_VALUES: Set[EInvoiceSummaryContainer] = {
    "pdf",
}


def check_e_invoice_summary_container(value: str) -> EInvoiceSummaryContainer:
    if value in E_INVOICE_SUMMARY_CONTAINER_VALUES:
        return cast(EInvoiceSummaryContainer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_CONTAINER_VALUES!r}"
    )
