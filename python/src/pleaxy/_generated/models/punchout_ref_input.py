from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PunchoutRefInput")


@_attrs_define
class PunchoutRefInput:
    """
    Attributes:
        session_id (str):  Example: SS-0123456789ABCDEF0123456789ABCDEF.
        cart_line_no (float):
    """

    session_id: str
    cart_line_no: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id

        cart_line_no = self.cart_line_no

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sessionId": session_id,
                "cartLineNo": cart_line_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("sessionId")

        cart_line_no = d.pop("cartLineNo")

        punchout_ref_input = cls(
            session_id=session_id,
            cart_line_no=cart_line_no,
        )

        punchout_ref_input.additional_properties = d
        return punchout_ref_input

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
