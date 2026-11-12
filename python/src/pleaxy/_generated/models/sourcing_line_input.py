from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingLineInput")


@_attrs_define
class SourcingLineInput:
    """
    Attributes:
        name (str): What is asked for, 1–200 characters.
        qty (float): How many.
        id (Union[Unset, str]): The line's id, kept across edits so answers stay on it. Absent on a new line: the server
            gives one.
        unit (Union[Unset, str]): e.g. each, hour, month.
        needed_by (Union[Unset, str]): When it is needed, YYYY-MM-DD. The comparison tells whether each answer's lead
            time meets it.
        notes (Union[Unset, str]): Specifications or notes for suppliers, up to 2,000 characters.
        target_unit_price (Union[Unset, float]): The buyer's target unit price. Buyer-only: never shown to a supplier.
    """

    name: str
    qty: float
    id: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    needed_by: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    target_unit_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        qty = self.qty

        id = self.id

        unit = self.unit

        needed_by = self.needed_by

        notes = self.notes

        target_unit_price = self.target_unit_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "qty": qty,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        name = d.pop("name")

        qty = d.pop("qty")

        id = d.pop("id", UNSET)

        unit = d.pop("unit", UNSET)

        needed_by = d.pop("neededBy", UNSET)

        notes = d.pop("notes", UNSET)

        target_unit_price = d.pop("targetUnitPrice", UNSET)

        sourcing_line_input = cls(
            name=name,
            qty=qty,
            id=id,
            unit=unit,
            needed_by=needed_by,
            notes=notes,
            target_unit_price=target_unit_price,
        )

        sourcing_line_input.additional_properties = d
        return sourcing_line_input

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
