from typing import Literal, Set, cast

ModuleOfferItem = Literal[
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "procureToPay",
    "receipt",
    "request",
    "source",
    "sourcing",
    "suite",
    "suppliers",
]

MODULE_OFFER_ITEM_VALUES: Set[ModuleOfferItem] = {
    "aiSpend",
    "contracts",
    "invoice",
    "order",
    "payment",
    "procureToPay",
    "receipt",
    "request",
    "source",
    "sourcing",
    "suite",
    "suppliers",
}


def check_module_offer_item(value: str) -> ModuleOfferItem:
    if value in MODULE_OFFER_ITEM_VALUES:
        return cast(ModuleOfferItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODULE_OFFER_ITEM_VALUES!r}"
    )
