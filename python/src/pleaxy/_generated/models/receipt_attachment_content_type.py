from typing import Literal, Set, cast

ReceiptAttachmentContentType = Literal["application/pdf", "image/jpeg", "image/png"]

RECEIPT_ATTACHMENT_CONTENT_TYPE_VALUES: Set[ReceiptAttachmentContentType] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_receipt_attachment_content_type(value: str) -> ReceiptAttachmentContentType:
    if value in RECEIPT_ATTACHMENT_CONTENT_TYPE_VALUES:
        return cast(ReceiptAttachmentContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECEIPT_ATTACHMENT_CONTENT_TYPE_VALUES!r}"
    )
