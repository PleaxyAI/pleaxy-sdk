from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geography_preset_id import GeographyPresetId, check_geography_preset_id
from ..types import UNSET, Unset

T = TypeVar("T", bound="Geography")


@_attrs_define
class Geography:
    """
    Attributes:
        preset_id (Union[Unset, GeographyPresetId]):
        preset_version (Union[Unset, str]):
    """

    preset_id: Union[Unset, GeographyPresetId] = UNSET
    preset_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preset_id: Union[Unset, str] = UNSET
        if not isinstance(self.preset_id, Unset):
            preset_id = self.preset_id

        preset_version = self.preset_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preset_id is not UNSET:
            field_dict["presetId"] = preset_id
        if preset_version is not UNSET:
            field_dict["presetVersion"] = preset_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _preset_id = d.pop("presetId", UNSET)
        preset_id: Union[Unset, GeographyPresetId]
        if isinstance(_preset_id, Unset):
            preset_id = UNSET
        else:
            preset_id = check_geography_preset_id(_preset_id)

        preset_version = d.pop("presetVersion", UNSET)

        geography = cls(
            preset_id=preset_id,
            preset_version=preset_version,
        )

        geography.additional_properties = d
        return geography

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
