from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_meeting_view_attendee_side import (
    CommentMeetingViewAttendeeSide,
    check_comment_meeting_view_attendee_side,
)
from ..models.comment_meeting_view_closed_by_side import (
    CommentMeetingViewClosedBySide,
    check_comment_meeting_view_closed_by_side,
)
from ..models.comment_meeting_view_proposed_by import (
    CommentMeetingViewProposedBy,
    check_comment_meeting_view_proposed_by,
)
from ..models.comment_meeting_view_status import (
    CommentMeetingViewStatus,
    check_comment_meeting_view_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_meeting_attendee import CommentMeetingAttendee


T = TypeVar("T", bound="CommentMeetingView")


@_attrs_define
class CommentMeetingView:
    """
    Attributes:
        status (Union[Unset, CommentMeetingViewStatus]):
        attendees (Union[Unset, List['CommentMeetingAttendee']]):
        can_answer (Union[Unset, bool]):
        can_propose (Union[Unset, bool]):
        can_cancel (Union[Unset, bool]):
        updated_at (Union[Unset, str]):
        link (Union[Unset, str]):
        topic (Union[Unset, str]):
        duration_minutes (Union[Unset, float]):
        time_zone (Union[Unset, str]):
        times (Union[Unset, List[str]]):
        proposed_by (Union[Unset, CommentMeetingViewProposedBy]):
        proposer_name (Union[Unset, str]):
        counter_proposals (Union[Unset, float]):
        accepted_time (Union[Unset, str]):
        attendee_name (Union[Unset, str]):
        attendee_side (Union[Unset, CommentMeetingViewAttendeeSide]):
        decline_reason (Union[Unset, str]):
        closed_by_side (Union[Unset, CommentMeetingViewClosedBySide]):
        closed_by_name (Union[Unset, str]):
    """

    status: Union[Unset, CommentMeetingViewStatus] = UNSET
    attendees: Union[Unset, List["CommentMeetingAttendee"]] = UNSET
    can_answer: Union[Unset, bool] = UNSET
    can_propose: Union[Unset, bool] = UNSET
    can_cancel: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    duration_minutes: Union[Unset, float] = UNSET
    time_zone: Union[Unset, str] = UNSET
    times: Union[Unset, List[str]] = UNSET
    proposed_by: Union[Unset, CommentMeetingViewProposedBy] = UNSET
    proposer_name: Union[Unset, str] = UNSET
    counter_proposals: Union[Unset, float] = UNSET
    accepted_time: Union[Unset, str] = UNSET
    attendee_name: Union[Unset, str] = UNSET
    attendee_side: Union[Unset, CommentMeetingViewAttendeeSide] = UNSET
    decline_reason: Union[Unset, str] = UNSET
    closed_by_side: Union[Unset, CommentMeetingViewClosedBySide] = UNSET
    closed_by_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        attendees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        can_answer = self.can_answer

        can_propose = self.can_propose

        can_cancel = self.can_cancel

        updated_at = self.updated_at

        link = self.link

        topic = self.topic

        duration_minutes = self.duration_minutes

        time_zone = self.time_zone

        times: Union[Unset, List[str]] = UNSET
        if not isinstance(self.times, Unset):
            times = self.times

        proposed_by: Union[Unset, str] = UNSET
        if not isinstance(self.proposed_by, Unset):
            proposed_by = self.proposed_by

        proposer_name = self.proposer_name

        counter_proposals = self.counter_proposals

        accepted_time = self.accepted_time

        attendee_name = self.attendee_name

        attendee_side: Union[Unset, str] = UNSET
        if not isinstance(self.attendee_side, Unset):
            attendee_side = self.attendee_side

        decline_reason = self.decline_reason

        closed_by_side: Union[Unset, str] = UNSET
        if not isinstance(self.closed_by_side, Unset):
            closed_by_side = self.closed_by_side

        closed_by_name = self.closed_by_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if can_answer is not UNSET:
            field_dict["canAnswer"] = can_answer
        if can_propose is not UNSET:
            field_dict["canPropose"] = can_propose
        if can_cancel is not UNSET:
            field_dict["canCancel"] = can_cancel
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if link is not UNSET:
            field_dict["link"] = link
        if topic is not UNSET:
            field_dict["topic"] = topic
        if duration_minutes is not UNSET:
            field_dict["durationMinutes"] = duration_minutes
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if times is not UNSET:
            field_dict["times"] = times
        if proposed_by is not UNSET:
            field_dict["proposedBy"] = proposed_by
        if proposer_name is not UNSET:
            field_dict["proposerName"] = proposer_name
        if counter_proposals is not UNSET:
            field_dict["counterProposals"] = counter_proposals
        if accepted_time is not UNSET:
            field_dict["acceptedTime"] = accepted_time
        if attendee_name is not UNSET:
            field_dict["attendeeName"] = attendee_name
        if attendee_side is not UNSET:
            field_dict["attendeeSide"] = attendee_side
        if decline_reason is not UNSET:
            field_dict["declineReason"] = decline_reason
        if closed_by_side is not UNSET:
            field_dict["closedBySide"] = closed_by_side
        if closed_by_name is not UNSET:
            field_dict["closedByName"] = closed_by_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_meeting_attendee import CommentMeetingAttendee

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CommentMeetingViewStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_comment_meeting_view_status(_status)

        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = CommentMeetingAttendee.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        can_answer = d.pop("canAnswer", UNSET)

        can_propose = d.pop("canPropose", UNSET)

        can_cancel = d.pop("canCancel", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        link = d.pop("link", UNSET)

        topic = d.pop("topic", UNSET)

        duration_minutes = d.pop("durationMinutes", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        times = cast(List[str], d.pop("times", UNSET))

        _proposed_by = d.pop("proposedBy", UNSET)
        proposed_by: Union[Unset, CommentMeetingViewProposedBy]
        if isinstance(_proposed_by, Unset):
            proposed_by = UNSET
        else:
            proposed_by = check_comment_meeting_view_proposed_by(_proposed_by)

        proposer_name = d.pop("proposerName", UNSET)

        counter_proposals = d.pop("counterProposals", UNSET)

        accepted_time = d.pop("acceptedTime", UNSET)

        attendee_name = d.pop("attendeeName", UNSET)

        _attendee_side = d.pop("attendeeSide", UNSET)
        attendee_side: Union[Unset, CommentMeetingViewAttendeeSide]
        if isinstance(_attendee_side, Unset):
            attendee_side = UNSET
        else:
            attendee_side = check_comment_meeting_view_attendee_side(_attendee_side)

        decline_reason = d.pop("declineReason", UNSET)

        _closed_by_side = d.pop("closedBySide", UNSET)
        closed_by_side: Union[Unset, CommentMeetingViewClosedBySide]
        if isinstance(_closed_by_side, Unset):
            closed_by_side = UNSET
        else:
            closed_by_side = check_comment_meeting_view_closed_by_side(_closed_by_side)

        closed_by_name = d.pop("closedByName", UNSET)

        comment_meeting_view = cls(
            status=status,
            attendees=attendees,
            can_answer=can_answer,
            can_propose=can_propose,
            can_cancel=can_cancel,
            updated_at=updated_at,
            link=link,
            topic=topic,
            duration_minutes=duration_minutes,
            time_zone=time_zone,
            times=times,
            proposed_by=proposed_by,
            proposer_name=proposer_name,
            counter_proposals=counter_proposals,
            accepted_time=accepted_time,
            attendee_name=attendee_name,
            attendee_side=attendee_side,
            decline_reason=decline_reason,
            closed_by_side=closed_by_side,
            closed_by_name=closed_by_name,
        )

        comment_meeting_view.additional_properties = d
        return comment_meeting_view

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
