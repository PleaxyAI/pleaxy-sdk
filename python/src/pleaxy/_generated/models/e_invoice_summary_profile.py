from typing import Literal, Set, cast

EInvoiceSummaryProfile = Literal[
    "en16931",
    "factur-x-basic",
    "factur-x-basic-wl",
    "factur-x-extended",
    "factur-x-minimum",
    "fatturapa",
    "other",
    "peppol-bis-billing-3",
    "xrechnung",
    "xrechnung-extension",
]

E_INVOICE_SUMMARY_PROFILE_VALUES: Set[EInvoiceSummaryProfile] = {
    "en16931",
    "factur-x-basic",
    "factur-x-basic-wl",
    "factur-x-extended",
    "factur-x-minimum",
    "fatturapa",
    "other",
    "peppol-bis-billing-3",
    "xrechnung",
    "xrechnung-extension",
}


def check_e_invoice_summary_profile(value: str) -> EInvoiceSummaryProfile:
    if value in E_INVOICE_SUMMARY_PROFILE_VALUES:
        return cast(EInvoiceSummaryProfile, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_PROFILE_VALUES!r}"
    )
