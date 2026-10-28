from typing import Literal, Set, cast

SupplierBankAccountLearnedFromSide = Literal["buyer", "supplier"]

SUPPLIER_BANK_ACCOUNT_LEARNED_FROM_SIDE_VALUES: Set[
    SupplierBankAccountLearnedFromSide
] = {
    "buyer",
    "supplier",
}


def check_supplier_bank_account_learned_from_side(
    value: str,
) -> SupplierBankAccountLearnedFromSide:
    if value in SUPPLIER_BANK_ACCOUNT_LEARNED_FROM_SIDE_VALUES:
        return cast(SupplierBankAccountLearnedFromSide, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_LEARNED_FROM_SIDE_VALUES!r}"
    )
