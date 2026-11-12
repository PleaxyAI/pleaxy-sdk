from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_comment_input_visibility import (
    CreateCommentInputVisibility,
    check_create_comment_input_visibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_meeting_input import CommentMeetingInput


T = TypeVar("T", bound="CreateCommentInput")


@_attrs_define
class CreateCommentInput:
    """
    Attributes:
        body (str): Plain text. Line breaks are kept; control, bidi and invisible characters are removed.
        visibility (CreateCommentInputVisibility): internal: your own team only. shared: the other side of the
            relationship reads and answers it too. A supplier's comments are always shared.
        mentions (Union[Unset, List[str]]): Employee keys of people in your own workspace to notify.
        meeting (Union[Unset, CommentMeetingInput]):
    """

    body: str
    visibility: CreateCommentInputVisibility
    mentions: Union[Unset, List[str]] = UNSET
    meeting: Union[Unset, "CommentMeetingInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        body = self.body

        visibility: str = self.visibility

        mentions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = self.mentions

        meeting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meeting, Unset):
            meeting = self.meeting.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "visibility": visibility,
            }
        )
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if meeting is not UNSET:
            field_dict["meeting"] = meeting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_meeting_input import CommentMeetingInput

        d = src_dict.copy()
        body = d.pop("body")

        visibility = check_create_comment_input_visibility(d.pop("visibility"))

        mentions = cast(List[str], d.pop("mentions", UNSET))

        _meeting = d.pop("meeting", UNSET)
        meeting: Union[Unset, CommentMeetingInput]
        if isinstance(_meeting, Unset):
            meeting = UNSET
        else:
            meeting = CommentMeetingInput.from_dict(_meeting)

        create_comment_input = cls(
            body=body,
            visibility=visibility,
            mentions=mentions,
            meeting=meeting,
        )

        create_comment_input.additional_properties = d
        return create_comment_input

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
