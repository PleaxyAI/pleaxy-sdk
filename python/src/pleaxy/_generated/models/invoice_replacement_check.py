from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceReplacementCheck")


@_attrs_define
class InvoiceReplacementCheck:
    """
    Attributes:
        credited_in_full (Union[Unset, bool]):
        uncredited (Union[Unset, float]):
    """

    credited_in_full: Union[Unset, bool] = UNSET
    uncredited: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credited_in_full = self.credited_in_full

        uncredited = self.uncredited

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credited_in_full is not UNSET:
            field_dict["creditedInFull"] = credited_in_full
        if uncredited is not UNSET:
            field_dict["uncredited"] = uncredited

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credited_in_full = d.pop("creditedInFull", UNSET)

        uncredited = d.pop("uncredited", UNSET)

        invoice_replacement_check = cls(
            credited_in_full=credited_in_full,
            uncredited=uncredited,
        )

        invoice_replacement_check.additional_properties = d
        return invoice_replacement_check

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
