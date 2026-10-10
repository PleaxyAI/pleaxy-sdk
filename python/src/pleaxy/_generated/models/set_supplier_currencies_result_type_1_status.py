from typing import Literal, Set, cast

SetSupplierCurrenciesResultType1Status = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_STATUS_VALUES: Set[
    SetSupplierCurrenciesResultType1Status
] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_set_supplier_currencies_result_type_1_status(
    value: str,
) -> SetSupplierCurrenciesResultType1Status:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_STATUS_VALUES:
        return cast(SetSupplierCurrenciesResultType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_STATUS_VALUES!r}"
    )
