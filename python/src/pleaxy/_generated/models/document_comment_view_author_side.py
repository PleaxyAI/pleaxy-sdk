from typing import Literal, Set, cast

DocumentCommentViewAuthorSide = Literal["buyer", "supplier"]

DOCUMENT_COMMENT_VIEW_AUTHOR_SIDE_VALUES: Set[DocumentCommentViewAuthorSide] = {
    "buyer",
    "supplier",
}


def check_document_comment_view_author_side(
    value: str,
) -> DocumentCommentViewAuthorSide:
    if value in DOCUMENT_COMMENT_VIEW_AUTHOR_SIDE_VALUES:
        return cast(DocumentCommentViewAuthorSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_COMMENT_VIEW_AUTHOR_SIDE_VALUES!r}"
    )
