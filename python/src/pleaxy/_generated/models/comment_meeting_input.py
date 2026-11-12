from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_meeting_input_duration_minutes import (
    CommentMeetingInputDurationMinutes,
    check_comment_meeting_input_duration_minutes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentMeetingInput")


@_attrs_define
class CommentMeetingInput:
    """
    Attributes:
        topic (str): What the meeting is about, on one line.
        duration_minutes (CommentMeetingInputDurationMinutes): How long the meeting lasts, in minutes.
        time_zone (str): Your time zone, as an IANA name such as Europe/Madrid.
        times (List[str]): Two or three proposed start times, ISO 8601 with an offset, in the future.
        link (Union[Unset, str]): An https link to the call.
    """

    topic: str
    duration_minutes: CommentMeetingInputDurationMinutes
    time_zone: str
    times: List[str]
    link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        topic = self.topic

        duration_minutes: int = self.duration_minutes

        time_zone = self.time_zone

        times = self.times

        link = self.link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
                "durationMinutes": duration_minutes,
                "timeZone": time_zone,
                "times": times,
            }
        )
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        topic = d.pop("topic")

        duration_minutes = check_comment_meeting_input_duration_minutes(
            d.pop("durationMinutes")
        )

        time_zone = d.pop("timeZone")

        times = cast(List[str], d.pop("times"))

        link = d.pop("link", UNSET)

        comment_meeting_input = cls(
            topic=topic,
            duration_minutes=duration_minutes,
            time_zone=time_zone,
            times=times,
            link=link,
        )

        comment_meeting_input.additional_properties = d
        return comment_meeting_input

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
