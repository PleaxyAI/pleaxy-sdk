from typing import Literal, Set, cast

PurchaseOrderQuoteDocumentDocumentType = Literal[
    "contract", "invoice", "order_form", "other", "proforma", "quote", "sow"
]

PURCHASE_ORDER_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES: Set[
    PurchaseOrderQuoteDocumentDocumentType
] = {
    "contract",
    "invoice",
    "order_form",
    "other",
    "proforma",
    "quote",
    "sow",
}


def check_purchase_order_quote_document_document_type(
    value: str,
) -> PurchaseOrderQuoteDocumentDocumentType:
    if value in PURCHASE_ORDER_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES:
        return cast(PurchaseOrderQuoteDocumentDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES!r}"
    )
