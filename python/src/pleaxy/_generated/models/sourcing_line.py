from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingLine")


@_attrs_define
class SourcingLine:
    """
    Attributes:
        id (str):
        name (Union[Unset, str]):
        qty (Union[Unset, float]):
        unit (Union[Unset, str]):
        needed_by (Union[Unset, str]):
        notes (Union[Unset, str]):
        target_unit_price (Union[Unset, float]):
    """

    id: str
    name: Union[Unset, str] = UNSET
    qty: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    needed_by: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    target_unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        qty = self.qty

        unit = self.unit

        needed_by = self.needed_by

        notes = self.notes

        target_unit_price = self.target_unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit is not UNSET:
            field_dict["unit"] = unit
        if needed_by is not UNSET:
            field_dict["neededBy"] = needed_by
        if notes is not UNSET:
            field_dict["notes"] = notes
        if target_unit_price is not UNSET:
            field_dict["targetUnitPrice"] = target_unit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        qty = d.pop("qty", UNSET)

        unit = d.pop("unit", UNSET)

        needed_by = d.pop("neededBy", UNSET)

        notes = d.pop("notes", UNSET)

        target_unit_price = d.pop("targetUnitPrice", UNSET)

        sourcing_line = cls(
            id=id,
            name=name,
            qty=qty,
            unit=unit,
            needed_by=needed_by,
            notes=notes,
            target_unit_price=target_unit_price,
        )

        sourcing_line.additional_properties = d
        return sourcing_line

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
