from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemPunchoutRef")


@_attrs_define
class LineItemPunchoutRef:
    """
    Attributes:
        session_id (Union[Unset, str]):
        cart_line_no (Union[Unset, float]):
    """

    session_id: Union[Unset, str] = UNSET
    cart_line_no: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id

        cart_line_no = self.cart_line_no

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if cart_line_no is not UNSET:
            field_dict["cartLineNo"] = cart_line_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("sessionId", UNSET)

        cart_line_no = d.pop("cartLineNo", UNSET)

        line_item_punchout_ref = cls(
            session_id=session_id,
            cart_line_no=cart_line_no,
        )

        line_item_punchout_ref.additional_properties = d
        return line_item_punchout_ref

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
