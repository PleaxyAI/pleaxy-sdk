from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierScreeningListVersions")


@_attrs_define
class SupplierScreeningListVersions:
    """
    Attributes:
        eu (Union[Unset, str]):
        uk (Union[Unset, str]):
        ofac (Union[Unset, str]):
        un (Union[Unset, str]):
    """

    eu: Union[Unset, str] = UNSET
    uk: Union[Unset, str] = UNSET
    ofac: Union[Unset, str] = UNSET
    un: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eu = self.eu

        uk = self.uk

        ofac = self.ofac

        un = self.un

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eu is not UNSET:
            field_dict["eu"] = eu
        if uk is not UNSET:
            field_dict["uk"] = uk
        if ofac is not UNSET:
            field_dict["ofac"] = ofac
        if un is not UNSET:
            field_dict["un"] = un

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eu = d.pop("eu", UNSET)

        uk = d.pop("uk", UNSET)

        ofac = d.pop("ofac", UNSET)

        un = d.pop("un", UNSET)

        supplier_screening_list_versions = cls(
            eu=eu,
            uk=uk,
            ofac=ofac,
            un=un,
        )

        supplier_screening_list_versions.additional_properties = d
        return supplier_screening_list_versions

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
