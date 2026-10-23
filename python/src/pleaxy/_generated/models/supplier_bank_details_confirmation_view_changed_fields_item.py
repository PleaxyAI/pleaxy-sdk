from typing import Literal, Set, cast

SupplierBankDetailsConfirmationViewChangedFieldsItem = Literal[
    "accountNumber",
    "bic",
    "iban",
    "mailingAddress",
    "method",
    "notes",
    "payeeName",
    "routingNumber",
]

SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CHANGED_FIELDS_ITEM_VALUES: Set[
    SupplierBankDetailsConfirmationViewChangedFieldsItem
] = {
    "accountNumber",
    "bic",
    "iban",
    "mailingAddress",
    "method",
    "notes",
    "payeeName",
    "routingNumber",
}


def check_supplier_bank_details_confirmation_view_changed_fields_item(
    value: str,
) -> SupplierBankDetailsConfirmationViewChangedFieldsItem:
    if value in SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CHANGED_FIELDS_ITEM_VALUES:
        return cast(SupplierBankDetailsConfirmationViewChangedFieldsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_BANK_DETAILS_CONFIRMATION_VIEW_CHANGED_FIELDS_ITEM_VALUES!r}"
    )
