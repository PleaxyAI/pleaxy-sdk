from typing import Literal, Set, cast

SupplierBankAccountStatus = Literal["changing", "unverified", "verified"]

SUPPLIER_BANK_ACCOUNT_STATUS_VALUES: Set[SupplierBankAccountStatus] = {
    "changing",
    "unverified",
    "verified",
}


def check_supplier_bank_account_status(value: str) -> SupplierBankAccountStatus:
    if value in SUPPLIER_BANK_ACCOUNT_STATUS_VALUES:
        return cast(SupplierBankAccountStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_STATUS_VALUES!r}"
    )
