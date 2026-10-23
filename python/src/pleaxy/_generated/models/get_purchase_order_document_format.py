from typing import Literal, Set, cast

GetPurchaseOrderDocumentFormat = Literal["cxml", "ubl"]

GET_PURCHASE_ORDER_DOCUMENT_FORMAT_VALUES: Set[GetPurchaseOrderDocumentFormat] = {
    "cxml",
    "ubl",
}


def check_get_purchase_order_document_format(
    value: str,
) -> GetPurchaseOrderDocumentFormat:
    if value in GET_PURCHASE_ORDER_DOCUMENT_FORMAT_VALUES:
        return cast(GetPurchaseOrderDocumentFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PURCHASE_ORDER_DOCUMENT_FORMAT_VALUES!r}"
    )
