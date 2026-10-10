from typing import Literal, Set, cast

RemittanceCheckChangedFieldsItem = Literal[
    "accountNumber",
    "bic",
    "iban",
    "mailingAddress",
    "method",
    "notes",
    "payeeName",
    "routingNumber",
]

REMITTANCE_CHECK_CHANGED_FIELDS_ITEM_VALUES: Set[RemittanceCheckChangedFieldsItem] = {
    "accountNumber",
    "bic",
    "iban",
    "mailingAddress",
    "method",
    "notes",
    "payeeName",
    "routingNumber",
}


def check_remittance_check_changed_fields_item(
    value: str,
) -> RemittanceCheckChangedFieldsItem:
    if value in REMITTANCE_CHECK_CHANGED_FIELDS_ITEM_VALUES:
        return cast(RemittanceCheckChangedFieldsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_CHECK_CHANGED_FIELDS_ITEM_VALUES!r}"
    )
