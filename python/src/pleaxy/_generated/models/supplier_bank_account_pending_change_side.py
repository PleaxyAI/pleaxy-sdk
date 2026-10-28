from typing import Literal, Set, cast

SupplierBankAccountPendingChangeSide = Literal["buyer", "supplier"]

SUPPLIER_BANK_ACCOUNT_PENDING_CHANGE_SIDE_VALUES: Set[
    SupplierBankAccountPendingChangeSide
] = {
    "buyer",
    "supplier",
}


def check_supplier_bank_account_pending_change_side(
    value: str,
) -> SupplierBankAccountPendingChangeSide:
    if value in SUPPLIER_BANK_ACCOUNT_PENDING_CHANGE_SIDE_VALUES:
        return cast(SupplierBankAccountPendingChangeSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_PENDING_CHANGE_SIDE_VALUES!r}"
    )
