from typing import Literal, Set, cast

SupplierBankAccountApprovalVerification = Literal[
    "buyer_approved", "paid_before", "supplier_confirmed"
]

SUPPLIER_BANK_ACCOUNT_APPROVAL_VERIFICATION_VALUES: Set[
    SupplierBankAccountApprovalVerification
] = {
    "buyer_approved",
    "paid_before",
    "supplier_confirmed",
}


def check_supplier_bank_account_approval_verification(
    value: str,
) -> SupplierBankAccountApprovalVerification:
    if value in SUPPLIER_BANK_ACCOUNT_APPROVAL_VERIFICATION_VALUES:
        return cast(SupplierBankAccountApprovalVerification, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_ACCOUNT_APPROVAL_VERIFICATION_VALUES!r}"
    )
