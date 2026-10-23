from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ShipNoticeLineInput")


@_attrs_define
class ShipNoticeLineInput:
    """
    Attributes:
        line_no (float):
        qty (float):
    """

    line_no: float
    qty: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        qty = self.qty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNo": line_no,
                "qty": qty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo")

        qty = d.pop("qty")

        ship_notice_line_input = cls(
            line_no=line_no,
            qty=qty,
        )

        ship_notice_line_input.additional_properties = d
        return ship_notice_line_input

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
