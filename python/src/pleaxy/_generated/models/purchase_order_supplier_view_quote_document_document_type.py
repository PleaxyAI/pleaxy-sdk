from typing import Literal, Set, cast

PurchaseOrderSupplierViewQuoteDocumentDocumentType = Literal[
    "contract", "invoice", "order_form", "other", "proforma", "quote", "sow"
]

PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES: Set[
    PurchaseOrderSupplierViewQuoteDocumentDocumentType
] = {
    "contract",
    "invoice",
    "order_form",
    "other",
    "proforma",
    "quote",
    "sow",
}


def check_purchase_order_supplier_view_quote_document_document_type(
    value: str,
) -> PurchaseOrderSupplierViewQuoteDocumentDocumentType:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES:
        return cast(PurchaseOrderSupplierViewQuoteDocumentDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_QUOTE_DOCUMENT_DOCUMENT_TYPE_VALUES!r}"
    )
