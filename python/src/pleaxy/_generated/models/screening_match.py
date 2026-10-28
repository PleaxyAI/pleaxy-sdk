from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screening_match_closed_reason import (
    ScreeningMatchClosedReason,
    check_screening_match_closed_reason,
)
from ..models.screening_match_list import ScreeningMatchList, check_screening_match_list
from ..models.screening_match_state import (
    ScreeningMatchState,
    check_screening_match_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screen_subject import ScreenSubject
    from ..models.screening_match_decided_by import ScreeningMatchDecidedBy
    from ..models.screening_match_entry import ScreeningMatchEntry


T = TypeVar("T", bound="ScreeningMatch")


@_attrs_define
class ScreeningMatch:
    """
    Attributes:
        id (str):
        entry_id (Union[Unset, str]):
        list_ (Union[Unset, ScreeningMatchList]):
        entry_name (Union[Unset, str]):
        matched_name (Union[Unset, str]):
        subject (Union[Unset, ScreenSubject]):
        score (Union[Unset, float]):
        country_mismatch (Union[Unset, bool]):
        entry (Union[Unset, ScreeningMatchEntry]):
        list_version (Union[Unset, str]):
        state (Union[Unset, ScreeningMatchState]):
        found_at (Union[Unset, str]):
        decided_at (Union[Unset, str]):
        decided_by (Union[Unset, ScreeningMatchDecidedBy]):
        reason (Union[Unset, str]):
        closed_reason (Union[Unset, ScreeningMatchClosedReason]):
    """

    id: str
    entry_id: Union[Unset, str] = UNSET
    list_: Union[Unset, ScreeningMatchList] = UNSET
    entry_name: Union[Unset, str] = UNSET
    matched_name: Union[Unset, str] = UNSET
    subject: Union[Unset, "ScreenSubject"] = UNSET
    score: Union[Unset, float] = UNSET
    country_mismatch: Union[Unset, bool] = UNSET
    entry: Union[Unset, "ScreeningMatchEntry"] = UNSET
    list_version: Union[Unset, str] = UNSET
    state: Union[Unset, ScreeningMatchState] = UNSET
    found_at: Union[Unset, str] = UNSET
    decided_at: Union[Unset, str] = UNSET
    decided_by: Union[Unset, "ScreeningMatchDecidedBy"] = UNSET
    reason: Union[Unset, str] = UNSET
    closed_reason: Union[Unset, ScreeningMatchClosedReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        entry_id = self.entry_id

        list_: Union[Unset, str] = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_

        entry_name = self.entry_name

        matched_name = self.matched_name

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        score = self.score

        country_mismatch = self.country_mismatch

        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        list_version = self.list_version

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        found_at = self.found_at

        decided_at = self.decided_at

        decided_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.decided_by, Unset):
            decided_by = self.decided_by.to_dict()

        reason = self.reason

        closed_reason: Union[Unset, str] = UNSET
        if not isinstance(self.closed_reason, Unset):
            closed_reason = self.closed_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if list_ is not UNSET:
            field_dict["list"] = list_
        if entry_name is not UNSET:
            field_dict["entryName"] = entry_name
        if matched_name is not UNSET:
            field_dict["matchedName"] = matched_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if score is not UNSET:
            field_dict["score"] = score
        if country_mismatch is not UNSET:
            field_dict["countryMismatch"] = country_mismatch
        if entry is not UNSET:
            field_dict["entry"] = entry
        if list_version is not UNSET:
            field_dict["listVersion"] = list_version
        if state is not UNSET:
            field_dict["state"] = state
        if found_at is not UNSET:
            field_dict["foundAt"] = found_at
        if decided_at is not UNSET:
            field_dict["decidedAt"] = decided_at
        if decided_by is not UNSET:
            field_dict["decidedBy"] = decided_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if closed_reason is not UNSET:
            field_dict["closedReason"] = closed_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.screen_subject import ScreenSubject
        from ..models.screening_match_decided_by import ScreeningMatchDecidedBy
        from ..models.screening_match_entry import ScreeningMatchEntry

        d = src_dict.copy()
        id = d.pop("id")

        entry_id = d.pop("entryId", UNSET)

        _list_ = d.pop("list", UNSET)
        list_: Union[Unset, ScreeningMatchList]
        if isinstance(_list_, Unset):
            list_ = UNSET
        else:
            list_ = check_screening_match_list(_list_)

        entry_name = d.pop("entryName", UNSET)

        matched_name = d.pop("matchedName", UNSET)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, ScreenSubject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = ScreenSubject.from_dict(_subject)

        score = d.pop("score", UNSET)

        country_mismatch = d.pop("countryMismatch", UNSET)

        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, ScreeningMatchEntry]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = ScreeningMatchEntry.from_dict(_entry)

        list_version = d.pop("listVersion", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ScreeningMatchState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_screening_match_state(_state)

        found_at = d.pop("foundAt", UNSET)

        decided_at = d.pop("decidedAt", UNSET)

        _decided_by = d.pop("decidedBy", UNSET)
        decided_by: Union[Unset, ScreeningMatchDecidedBy]
        if isinstance(_decided_by, Unset):
            decided_by = UNSET
        else:
            decided_by = ScreeningMatchDecidedBy.from_dict(_decided_by)

        reason = d.pop("reason", UNSET)

        _closed_reason = d.pop("closedReason", UNSET)
        closed_reason: Union[Unset, ScreeningMatchClosedReason]
        if isinstance(_closed_reason, Unset):
            closed_reason = UNSET
        else:
            closed_reason = check_screening_match_closed_reason(_closed_reason)

        screening_match = cls(
            id=id,
            entry_id=entry_id,
            list_=list_,
            entry_name=entry_name,
            matched_name=matched_name,
            subject=subject,
            score=score,
            country_mismatch=country_mismatch,
            entry=entry,
            list_version=list_version,
            state=state,
            found_at=found_at,
            decided_at=decided_at,
            decided_by=decided_by,
            reason=reason,
            closed_reason=closed_reason,
        )

        screening_match.additional_properties = d
        return screening_match

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
