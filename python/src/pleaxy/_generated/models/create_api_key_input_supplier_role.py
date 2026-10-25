from typing import Literal, Set, cast

CreateApiKeyInputSupplierRole = Literal[
    "accounts-receivable", "administrator", "fulfillment", "read-only", "sales"
]

CREATE_API_KEY_INPUT_SUPPLIER_ROLE_VALUES: Set[CreateApiKeyInputSupplierRole] = {
    "accounts-receivable",
    "administrator",
    "fulfillment",
    "read-only",
    "sales",
}


def check_create_api_key_input_supplier_role(
    value: str,
) -> CreateApiKeyInputSupplierRole:
    if value in CREATE_API_KEY_INPUT_SUPPLIER_ROLE_VALUES:
        return cast(CreateApiKeyInputSupplierRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_INPUT_SUPPLIER_ROLE_VALUES!r}"
    )
