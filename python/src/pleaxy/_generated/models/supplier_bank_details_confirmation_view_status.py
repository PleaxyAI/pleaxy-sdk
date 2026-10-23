from typing import Literal, Set, cast

SupplierBankDetailsConfirmationViewStatus = Literal["confirmed", "disputed", "pending"]

SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_STATUS_VALUES: Set[
    SupplierBankDetailsConfirmationViewStatus
] = {
    "confirmed",
    "disputed",
    "pending",
}


def check_supplier_bank_details_confirmation_view_status(
    value: str,
) -> SupplierBankDetailsConfirmationViewStatus:
    if value in SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_STATUS_VALUES:
        return cast(SupplierBankDetailsConfirmationViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_STATUS_VALUES!r}"
    )
