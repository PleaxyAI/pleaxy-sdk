from typing import Literal, Set, cast

ModuleOfferKind = Literal["group", "module", "suite"]

MODULE_OFFER_KIND_VALUES: Set[ModuleOfferKind] = {
    "group",
    "module",
    "suite",
}


def check_module_offer_kind(value: str) -> ModuleOfferKind:
    if value in MODULE_OFFER_KIND_VALUES:
        return cast(ModuleOfferKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODULE_OFFER_KIND_VALUES!r}"
    )
