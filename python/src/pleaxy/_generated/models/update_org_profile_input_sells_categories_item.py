from typing import Literal, Set, cast

UpdateOrgProfileInputSellsCategoriesItem = Literal[
    "agriculture",
    "cloud-ai",
    "construction",
    "electrical",
    "facilities",
    "food",
    "healthcare",
    "industrial",
    "it-hardware",
    "it-services",
    "legal-finance",
    "logistics",
    "marketing-creative",
    "office",
    "packaging-print",
    "professional-services",
    "raw-materials",
    "safety-security",
    "software",
    "staffing",
    "training",
    "travel-events",
    "utilities-energy",
    "vehicles",
]

UPDATE_ORG_PROFILE_INPUT_SELLS_CATEGORIES_ITEM_VALUES: Set[
    UpdateOrgProfileInputSellsCategoriesItem
] = {
    "agriculture",
    "cloud-ai",
    "construction",
    "electrical",
    "facilities",
    "food",
    "healthcare",
    "industrial",
    "it-hardware",
    "it-services",
    "legal-finance",
    "logistics",
    "marketing-creative",
    "office",
    "packaging-print",
    "professional-services",
    "raw-materials",
    "safety-security",
    "software",
    "staffing",
    "training",
    "travel-events",
    "utilities-energy",
    "vehicles",
}


def check_update_org_profile_input_sells_categories_item(
    value: str,
) -> UpdateOrgProfileInputSellsCategoriesItem:
    if value in UPDATE_ORG_PROFILE_INPUT_SELLS_CATEGORIES_ITEM_VALUES:
        return cast(UpdateOrgProfileInputSellsCategoriesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ORG_PROFILE_INPUT_SELLS_CATEGORIES_ITEM_VALUES!r}"
    )
