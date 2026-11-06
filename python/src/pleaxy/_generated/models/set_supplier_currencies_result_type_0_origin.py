from typing import Literal, Set, cast

SetSupplierCurrenciesResultType0Origin = Literal["rfq"]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_ORIGIN_VALUES: Set[
    SetSupplierCurrenciesResultType0Origin
] = {
    "rfq",
}


def check_set_supplier_currencies_result_type_0_origin(
    value: str,
) -> SetSupplierCurrenciesResultType0Origin:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_ORIGIN_VALUES:
        return cast(SetSupplierCurrenciesResultType0Origin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_ORIGIN_VALUES!r}"
    )
