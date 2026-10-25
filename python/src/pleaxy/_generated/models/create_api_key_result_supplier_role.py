from typing import Literal, Set, cast

CreateApiKeyResultSupplierRole = Literal[
    "accounts-receivable",
    "administrator",
    "fulfillment",
    "member",
    "read-only",
    "sales",
]

CREATE_API_KEY_RESULT_SUPPLIER_ROLE_VALUES: Set[CreateApiKeyResultSupplierRole] = {
    "accounts-receivable",
    "administrator",
    "fulfillment",
    "member",
    "read-only",
    "sales",
}


def check_create_api_key_result_supplier_role(
    value: str,
) -> CreateApiKeyResultSupplierRole:
    if value in CREATE_API_KEY_RESULT_SUPPLIER_ROLE_VALUES:
        return cast(CreateApiKeyResultSupplierRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_RESULT_SUPPLIER_ROLE_VALUES!r}"
    )
