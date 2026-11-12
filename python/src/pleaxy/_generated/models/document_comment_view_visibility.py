from typing import Literal, Set, cast

DocumentCommentViewVisibility = Literal["internal", "shared"]

DOCUMENT_COMMENT_VIEW_VISIBILITY_VALUES: Set[DocumentCommentViewVisibility] = {
    "internal",
    "shared",
}


def check_document_comment_view_visibility(value: str) -> DocumentCommentViewVisibility:
    if value in DOCUMENT_COMMENT_VIEW_VISIBILITY_VALUES:
        return cast(DocumentCommentViewVisibility, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENT_COMMENT_VIEW_VISIBILITY_VALUES!r}"
    )
