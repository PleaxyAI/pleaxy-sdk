from typing import Literal, Set, cast

SupplierBankDetailsConfirmationViewConfirmedVia = Literal["phone", "supplier"]

SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CONFIRMED_VIA_VALUES: Set[
    SupplierBankDetailsConfirmationViewConfirmedVia
] = {
    "phone",
    "supplier",
}


def check_supplier_bank_details_confirmation_view_confirmed_via(
    value: str,
) -> SupplierBankDetailsConfirmationViewConfirmedVia:
    if value in SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CONFIRMED_VIA_VALUES:
        return cast(SupplierBankDetailsConfirmationViewConfirmedVia, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CONFIRMED_VIA_VALUES!r}"
    )
