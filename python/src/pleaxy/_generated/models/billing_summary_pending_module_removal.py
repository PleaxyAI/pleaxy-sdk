from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_summary_pending_module_removal_modules_item import (
    BillingSummaryPendingModuleRemovalModulesItem,
    check_billing_summary_pending_module_removal_modules_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSummaryPendingModuleRemoval")


@_attrs_define
class BillingSummaryPendingModuleRemoval:
    """
    Attributes:
        modules (Union[Unset, List[BillingSummaryPendingModuleRemovalModulesItem]]):
        at (Union[Unset, str]):
    """

    modules: Union[Unset, List[BillingSummaryPendingModuleRemovalModulesItem]] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modules: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = []
            for modules_item_data in self.modules:
                modules_item: str = modules_item_data
                modules.append(modules_item)

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modules is not UNSET:
            field_dict["modules"] = modules
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modules = []
        _modules = d.pop("modules", UNSET)
        for modules_item_data in _modules or []:
            modules_item = check_billing_summary_pending_module_removal_modules_item(
                modules_item_data
            )

            modules.append(modules_item)

        at = d.pop("at", UNSET)

        billing_summary_pending_module_removal = cls(
            modules=modules,
            at=at,
        )

        billing_summary_pending_module_removal.additional_properties = d
        return billing_summary_pending_module_removal

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
