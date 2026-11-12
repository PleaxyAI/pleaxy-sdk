from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_meeting_attendee_side import (
    CommentMeetingAttendeeSide,
    check_comment_meeting_attendee_side,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentMeetingAttendee")


@_attrs_define
class CommentMeetingAttendee:
    """
    Attributes:
        side (Union[Unset, CommentMeetingAttendeeSide]):
        name (Union[Unset, str]):
        email (Union[Unset, str]):
    """

    side: Union[Unset, CommentMeetingAttendeeSide] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        side: Union[Unset, str] = UNSET
        if not isinstance(self.side, Unset):
            side = self.side

        name = self.name

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if side is not UNSET:
            field_dict["side"] = side
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _side = d.pop("side", UNSET)
        side: Union[Unset, CommentMeetingAttendeeSide]
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = check_comment_meeting_attendee_side(_side)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        comment_meeting_attendee = cls(
            side=side,
            name=name,
            email=email,
        )

        comment_meeting_attendee.additional_properties = d
        return comment_meeting_attendee

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
