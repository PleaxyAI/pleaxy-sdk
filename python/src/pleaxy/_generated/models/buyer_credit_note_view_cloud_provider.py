from typing import Literal, Set, cast

BuyerCreditNoteViewCloudProvider = Literal["aws", "azure", "gcp", "oci"]

BUYER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES: Set[BuyerCreditNoteViewCloudProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_buyer_credit_note_view_cloud_provider(
    value: str,
) -> BuyerCreditNoteViewCloudProvider:
    if value in BUYER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES:
        return cast(BuyerCreditNoteViewCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_CREDIT_NOTE_VIEW_CLOUD_PROVIDER_VALUES!r}"
    )
