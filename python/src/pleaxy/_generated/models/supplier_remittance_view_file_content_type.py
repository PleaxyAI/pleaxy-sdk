from typing import Literal, Set, cast

SupplierRemittanceViewFileContentType = Literal[
    "application/pdf", "image/jpeg", "image/png"
]

SUPPLIER_REMITTANCE_VIEW_FILE_CONTENT_TYPE_VALUES: Set[
    SupplierRemittanceViewFileContentType
] = {
    "application/pdf",
    "image/jpeg",
    "image/png",
}


def check_supplier_remittance_view_file_content_type(
    value: str,
) -> SupplierRemittanceViewFileContentType:
    if value in SUPPLIER_REMITTANCE_VIEW_FILE_CONTENT_TYPE_VALUES:
        return cast(SupplierRemittanceViewFileContentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_REMITTANCE_VIEW_FILE_CONTENT_TYPE_VALUES!r}"
    )
