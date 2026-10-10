from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_entry_input import BreakdownEntryInput


T = TypeVar("T", bound="BreakdownGroupInput")


@_attrs_define
class BreakdownGroupInput:
    """
    Attributes:
        total_amount (float):
        breakdown (Union[Unset, List['BreakdownEntryInput']]): At most 20. Must sum to totalAmount.
    """

    total_amount: float
    breakdown: Union[Unset, List["BreakdownEntryInput"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        breakdown: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = []
            for breakdown_item_data in self.breakdown:
                breakdown_item = breakdown_item_data.to_dict()
                breakdown.append(breakdown_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalAmount": total_amount,
            }
        )
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.breakdown_entry_input import BreakdownEntryInput

        d = src_dict.copy()
        total_amount = d.pop("totalAmount")

        breakdown = []
        _breakdown = d.pop("breakdown", UNSET)
        for breakdown_item_data in _breakdown or []:
            breakdown_item = BreakdownEntryInput.from_dict(breakdown_item_data)

            breakdown.append(breakdown_item)

        breakdown_group_input = cls(
            total_amount=total_amount,
            breakdown=breakdown,
        )

        breakdown_group_input.additional_properties = d
        return breakdown_group_input

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
