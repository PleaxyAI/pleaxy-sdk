from typing import Literal, Set, cast

SetSupplierCurrenciesResultType0Status = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_STATUS_VALUES: Set[
    SetSupplierCurrenciesResultType0Status
] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_set_supplier_currencies_result_type_0_status(
    value: str,
) -> SetSupplierCurrenciesResultType0Status:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_STATUS_VALUES:
        return cast(SetSupplierCurrenciesResultType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_STATUS_VALUES!r}"
    )
