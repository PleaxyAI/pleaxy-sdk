from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceAccessRemovalSsoMappingSaved")


@_attrs_define
class InvoiceAccessRemovalSsoMappingSaved:
    """
    Attributes:
        at (Union[Unset, str]):
        by_key (Union[Unset, str]):
        by_name (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    by_key: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        by_key = self.by_key

        by_name = self.by_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if by_key is not UNSET:
            field_dict["byKey"] = by_key
        if by_name is not UNSET:
            field_dict["byName"] = by_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        by_key = d.pop("byKey", UNSET)

        by_name = d.pop("byName", UNSET)

        invoice_access_removal_sso_mapping_saved = cls(
            at=at,
            by_key=by_key,
            by_name=by_name,
        )

        invoice_access_removal_sso_mapping_saved.additional_properties = d
        return invoice_access_removal_sso_mapping_saved

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
