from typing import Literal, Set, cast

PurchaseOrderSupplierViewQuoteDocumentContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES: Set[
    PurchaseOrderSupplierViewQuoteDocumentContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_purchase_order_supplier_view_quote_document_content_type(
    value: str,
) -> PurchaseOrderSupplierViewQuoteDocumentContentType:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES:
        return cast(PurchaseOrderSupplierViewQuoteDocumentContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_CONTENT_TYPE_VALUES!r}"
    )
