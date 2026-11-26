from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceSubmittedFormat = Literal[
    "cii", "cxml", "facturae", "fatturapa", "json", "nfe", "nfse", "ubl"
]

GET_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    GetInvoiceResultBuyerInvoiceSubmittedFormat
] = {
    "cii",
    "cxml",
    "facturae",
    "fatturapa",
    "json",
    "nfe",
    "nfse",
    "ubl",
}


def check_get_invoice_result_buyer_invoice_submitted_format(
    value: str,
) -> GetInvoiceResultBuyerInvoiceSubmittedFormat:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
