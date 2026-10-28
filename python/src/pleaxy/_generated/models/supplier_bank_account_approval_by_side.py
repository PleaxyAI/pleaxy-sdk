from typing import Literal, Set, cast

SupplierBankAccountApprovalBySide = Literal["buyer", "supplier"]

SUPPLIER_BANK_ACCOUNT_APPROVAL_BY_SIDE_VALUES: Set[
    SupplierBankAccountApprovalBySide
] = {
    "buyer",
    "supplier",
}


def check_supplier_bank_account_approval_by_side(
    value: str,
) -> SupplierBankAccountApprovalBySide:
    if value in SUPPLIER_BANK_ACCOUNT_APPROVAL_BY_SIDE_VALUES:
        return cast(SupplierBankAccountApprovalBySide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_APPROVAL_BY_SIDE_VALUES!r}"
    )
