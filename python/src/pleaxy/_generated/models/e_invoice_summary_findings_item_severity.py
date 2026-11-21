from typing import Literal, Set, cast

EInvoiceSummaryFindingsItemSeverity = Literal["fatal", "warning"]

E_INVOICE_SUMMARY_FINDINGS_ITEM_SEVERITY_VALUES: Set[
    EInvoiceSummaryFindingsItemSeverity
] = {
    "fatal",
    "warning",
}


def check_e_invoice_summary_findings_item_severity(
    value: str,
) -> EInvoiceSummaryFindingsItemSeverity:
    if value in E_INVOICE_SUMMARY_FINDINGS_ITEM_SEVERITY_VALUES:
        return cast(EInvoiceSummaryFindingsItemSeverity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_FINDINGS_ITEM_SEVERITY_VALUES!r}"
    )
