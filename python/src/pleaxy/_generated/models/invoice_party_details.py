from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePartyDetails")


@_attrs_define
class InvoicePartyDetails:
    """
    Attributes:
        name (Union[Unset, str]):
        address_lines (Union[Unset, List[str]]):
        tax_id (Union[Unset, str]):
        tax_id_label (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    address_lines: Union[Unset, List[str]] = UNSET
    tax_id: Union[Unset, str] = UNSET
    tax_id_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address_lines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.address_lines, Unset):
            address_lines = self.address_lines

        tax_id = self.tax_id

        tax_id_label = self.tax_id_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address_lines is not UNSET:
            field_dict["addressLines"] = address_lines
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if tax_id_label is not UNSET:
            field_dict["taxIdLabel"] = tax_id_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address_lines = cast(List[str], d.pop("addressLines", UNSET))

        tax_id = d.pop("taxId", UNSET)

        tax_id_label = d.pop("taxIdLabel", UNSET)

        invoice_party_details = cls(
            name=name,
            address_lines=address_lines,
            tax_id=tax_id,
            tax_id_label=tax_id_label,
        )

        invoice_party_details.additional_properties = d
        return invoice_party_details

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
