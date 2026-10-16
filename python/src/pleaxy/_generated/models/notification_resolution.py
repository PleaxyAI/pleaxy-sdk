from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_resolution_outcome import (
    NotificationResolutionOutcome,
    check_notification_resolution_outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationResolution")


@_attrs_define
class NotificationResolution:
    """
    Attributes:
        outcome (Union[Unset, NotificationResolutionOutcome]):
        at (Union[Unset, str]):
    """

    outcome: Union[Unset, NotificationResolutionOutcome] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, NotificationResolutionOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_notification_resolution_outcome(_outcome)

        at = d.pop("at", UNSET)

        notification_resolution = cls(
            outcome=outcome,
            at=at,
        )

        notification_resolution.additional_properties = d
        return notification_resolution

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
