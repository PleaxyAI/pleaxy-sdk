from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_export_summary import FocusExportSummary


T = TypeVar("T", bound="FocusExportList")


@_attrs_define
class FocusExportList:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        exports (Union[Unset, List['FocusExportSummary']]):
    """

    enabled: Union[Unset, bool] = UNSET
    exports: Union[Unset, List["FocusExportSummary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        exports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exports, Unset):
            exports = []
            for exports_item_data in self.exports:
                exports_item = exports_item_data.to_dict()
                exports.append(exports_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if exports is not UNSET:
            field_dict["exports"] = exports

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_export_summary import FocusExportSummary

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        exports = []
        _exports = d.pop("exports", UNSET)
        for exports_item_data in _exports or []:
            exports_item = FocusExportSummary.from_dict(exports_item_data)

            exports.append(exports_item)

        focus_export_list = cls(
            enabled=enabled,
            exports=exports,
        )

        focus_export_list.additional_properties = d
        return focus_export_list

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
