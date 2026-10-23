from typing import Literal, Set, cast

RemittanceViewRemittancesItemFileContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

REMITTANCE_VIEW_REMITTANCES_ITEM_FILE_CONTENT_TYPE_VALUES: Set[
    RemittanceViewRemittancesItemFileContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_remittance_view_remittances_item_file_content_type(
    value: str,
) -> RemittanceViewRemittancesItemFileContentType:
    if value in REMITTANCE_VIEW_REMITTANCES_ITEM_FILE_CONTENT_TYPE_VALUES:
        return cast(RemittanceViewRemittancesItemFileContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_VIEW_REMITTANCES_ITEM_FILE_CONTENT_TYPE_VALUES!r}"
    )
