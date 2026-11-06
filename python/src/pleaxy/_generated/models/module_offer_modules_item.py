from typing import Literal, Set, cast

ModuleOfferModulesItem = Literal[
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "receipt",
    "request",
    "sourcing",
    "suppliers",
]

MODULE_OFFER_MODULES_ITEM_VALUES: Set[ModuleOfferModulesItem] = {
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "receipt",
    "request",
    "sourcing",
    "suppliers",
}


def check_module_offer_modules_item(value: str) -> ModuleOfferModulesItem:
    if value in MODULE_OFFER_MODULES_ITEM_VALUES:
        return cast(ModuleOfferModulesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODULE_OFFER_MODULES_ITEM_VALUES!r}"
    )
