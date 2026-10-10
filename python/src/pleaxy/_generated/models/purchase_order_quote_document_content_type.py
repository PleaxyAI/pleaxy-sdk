from typing import Literal, Set, cast

PurchaseOrderQuoteDocumentContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

PURCHASE_ORDER_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES: Set[
    PurchaseOrderQuoteDocumentContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_purchase_order_quote_document_content_type(
    value: str,
) -> PurchaseOrderQuoteDocumentContentType:
    if value in PURCHASE_ORDER_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES:
        return cast(PurchaseOrderQuoteDocumentContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES!r}"
    )
