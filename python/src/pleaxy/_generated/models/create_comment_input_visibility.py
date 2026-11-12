from typing import Literal, Set, cast

CreateCommentInputVisibility = Literal["internal", "shared"]

CREATE_COMMENT_INPUT_VISIBILITY_VALUES: Set[CreateCommentInputVisibility] = {
    "internal",
    "shared",
}


def check_create_comment_input_visibility(value: str) -> CreateCommentInputVisibility:
    if value in CREATE_COMMENT_INPUT_VISIBILITY_VALUES:
        return cast(CreateCommentInputVisibility, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_COMMENT_INPUT_VISIBILITY_VALUES!r}"
    )
