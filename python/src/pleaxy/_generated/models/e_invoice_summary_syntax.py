from typing import Literal, Set, cast

EInvoiceSummarySyntax = Literal["cii", "fatturapa", "ubl"]

E_INVOICE_SUMMARY_SYNTAX_VALUES: Set[EInvoiceSummarySyntax] = {
    "cii",
    "fatturapa",
    "ubl",
}


def check_e_invoice_summary_syntax(value: str) -> EInvoiceSummarySyntax:
    if value in E_INVOICE_SUMMARY_SYNTAX_VALUES:
        return cast(EInvoiceSummarySyntax, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_SYNTAX_VALUES!r}"
    )
