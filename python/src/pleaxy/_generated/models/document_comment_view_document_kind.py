from typing import Literal, Set, cast

DocumentCommentViewDocumentKind = Literal["contract", "invoice", "purchase_order"]

DOCUMENT_COMMENT_VIEW_DOCUMENT_KIND_VALUES: Set[DocumentCommentViewDocumentKind] = {
    "contract",
    "invoice",
    "purchase_order",
}


def check_document_comment_view_document_kind(
    value: str,
) -> DocumentCommentViewDocumentKind:
    if value in DOCUMENT_COMMENT_VIEW_DOCUMENT_KIND_VALUES:
        return cast(DocumentCommentViewDocumentKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_COMMENT_VIEW_DOCUMENT_KIND_VALUES!r}"
    )
