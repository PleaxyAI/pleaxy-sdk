from typing import Literal, Set, cast

SetSupplierCurrenciesResultType1Origin = Literal["rfq"]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_ORIGIN_VALUES: Set[
    SetSupplierCurrenciesResultType1Origin
] = {
    "rfq",
}


def check_set_supplier_currencies_result_type_1_origin(
    value: str,
) -> SetSupplierCurrenciesResultType1Origin:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_ORIGIN_VALUES:
        return cast(SetSupplierCurrenciesResultType1Origin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_ORIGIN_VALUES!r}"
    )
