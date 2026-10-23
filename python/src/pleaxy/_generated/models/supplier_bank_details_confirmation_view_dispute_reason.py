from typing import Literal, Set, cast

SupplierBankDetailsConfirmationViewDisputeReason = Literal[
    "not_sent", "wrong_bank_details"
]

SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_DISPUTE_REASON_VALUES: Set[
    SupplierBankDetailsConfirmationViewDisputeReason
] = {
    "not_sent",
    "wrong_bank_details",
}


def check_supplier_bank_details_confirmation_view_dispute_reason(
    value: str,
) -> SupplierBankDetailsConfirmationViewDisputeReason:
    if value in SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_DISPUTE_REASON_VALUES:
        return cast(SupplierBankDetailsConfirmationViewDisputeReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_DISPUTE_REASON_VALUES!r}"
    )
