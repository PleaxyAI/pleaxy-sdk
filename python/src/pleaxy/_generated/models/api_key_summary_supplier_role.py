from typing import Literal, Set, cast

ApiKeySummarySupplierRole = Literal[
    "accounts-receivable",
    "administrator",
    "fulfillment",
    "member",
    "read-only",
    "sales",
]

API_KEY_SUMMARY_SUPPLIER_ROLE_VALUES: Set[ApiKeySummarySupplierRole] = {
    "accounts-receivable",
    "administrator",
    "fulfillment",
    "member",
    "read-only",
    "sales",
}


def check_api_key_summary_supplier_role(value: str) -> ApiKeySummarySupplierRole:
    if value in API_KEY_SUMMARY_SUPPLIER_ROLE_VALUES:
        return cast(ApiKeySummarySupplierRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_KEY_SUMMARY_SUPPLIER_ROLE_VALUES!r}"
    )
