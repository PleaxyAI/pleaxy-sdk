from typing import Literal, Set, cast

RequestRemittanceUploadInputContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

REQUEST_REMITTANCE_UPLOAD_INPUT_CONTENT_TYPE_VALUES: Set[
    RequestRemittanceUploadInputContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_request_remittance_upload_input_content_type(
    value: str,
) -> RequestRemittanceUploadInputContentType:
    if value in REQUEST_REMITTANCE_UPLOAD_INPUT_CONTENT_TYPE_VALUES:
        return cast(RequestRemittanceUploadInputContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_REMITTANCE_UPLOAD_INPUT_CONTENT_TYPE_VALUES!r}"
    )
