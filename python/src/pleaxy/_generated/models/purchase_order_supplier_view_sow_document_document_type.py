from typing import Literal, Set, cast

PurchaseOrderSupplierViewSowDocumentDocumentType = Literal[
    "contract", "invoice", "order_form", "other", "proforma", "quote", "sow"
]

PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_DOCUMENT_TYPE_VALUES: Set[
    PurchaseOrderSupplierViewSowDocumentDocumentType
] = {
    "contract",
    "invoice",
    "order_form",
    "other",
    "proforma",
    "quote",
    "sow",
}


def check_purchase_order_supplier_view_sow_document_document_type(
    value: str,
) -> PurchaseOrderSupplierViewSowDocumentDocumentType:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_DOCUMENT_TYPE_VALUES:
        return cast(PurchaseOrderSupplierViewSowDocumentDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_SOW_DOCUMENT_DOCUMENT_TYPE_VALUES!r}"
    )
