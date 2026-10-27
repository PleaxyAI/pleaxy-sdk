from typing import Literal, Set, cast

RequestFileUploadInputContentType = Literal[
    "application/msword",
    "application/pdf",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "image/jpeg",
    "image/png",
    "text/csv",
    "text/plain",
]

REQUEST_FILE_UPLOAD_INPUT_CONTENT_TYPE_VALUES: Set[
    RequestFileUploadInputContentType
] = {
    "application/msword",
    "application/pdf",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "image/jpeg",
    "image/png",
    "text/csv",
    "text/plain",
}


def check_request_file_upload_input_content_type(
    value: str,
) -> RequestFileUploadInputContentType:
    if value in REQUEST_FILE_UPLOAD_INPUT_CONTENT_TYPE_VALUES:
        return cast(RequestFileUploadInputContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_FILE_UPLOAD_INPUT_CONTENT_TYPE_VALUES!r}"
    )
