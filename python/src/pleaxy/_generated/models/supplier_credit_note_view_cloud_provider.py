from typing import Literal, Set, cast

SupplierCreditNoteViewCloudProvider = Literal["aws", "azure", "gcp", "oci"]

SUPPLIER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES: Set[
    SupplierCreditNoteViewCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_supplier_credit_note_view_cloud_provider(
    value: str,
) -> SupplierCreditNoteViewCloudProvider:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES:
        return cast(SupplierCreditNoteViewCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES!r}"
    )
