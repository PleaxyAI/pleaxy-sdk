from typing import Literal, Set, cast

PurchaseOrderSupplierViewSowDocumentContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_CONTENT_TYPE_VALUES: Set[
    PurchaseOrderSupplierViewSowDocumentContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_purchase_order_supplier_view_sow_document_content_type(
    value: str,
) -> PurchaseOrderSupplierViewSowDocumentContentType:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_CONTENT_TYPE_VALUES:
        return cast(PurchaseOrderSupplierViewSowDocumentContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_CONTENT_TYPE_VALUES!r}"
    )
