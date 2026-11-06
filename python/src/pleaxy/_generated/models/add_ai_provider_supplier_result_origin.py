from typing import Literal, Set, cast

AddAiProviderSupplierResultOrigin = Literal["rfq"]

ADD_AI_PROVIDER_SUPPLIER_RESULT_ORIGIN_VALUES: Set[
    AddAiProviderSupplierResultOrigin
] = {
    "rfq",
}


def check_add_ai_provider_supplier_result_origin(
    value: str,
) -> AddAiProviderSupplierResultOrigin:
    if value in ADD_AI_PROVIDER_SUPPLIER_RESULT_ORIGIN_VALUES:
        return cast(AddAiProviderSupplierResultOrigin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_AI_PROVIDER_SUPPLIER_RESULT_ORIGIN_VALUES!r}"
    )
