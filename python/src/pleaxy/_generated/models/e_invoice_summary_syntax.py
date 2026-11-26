from typing import Literal, Set, cast

EInvoiceSummarySyntax = Literal["cii", "facturae", "fatturapa", "nfe", "nfse", "ubl"]

E_INVOICE_SUMMARY_SYNTAX_VALUES: Set[EInvoiceSummarySyntax] = {
    "cii",
    "facturae",
    "fatturapa",
    "nfe",
    "nfse",
    "ubl",
}


def check_e_invoice_summary_syntax(value: str) -> EInvoiceSummarySyntax:
    if value in E_INVOICE_SUMMARY_SYNTAX_VALUES:
        return cast(EInvoiceSummarySyntax, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_SYNTAX_VALUES!r}"
    )
