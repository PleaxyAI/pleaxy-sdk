from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_run_failure_reason import (
    FocusRunFailureReason,
    check_focus_run_failure_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusRunFailure")


@_attrs_define
class FocusRunFailure:
    """
    Attributes:
        reason (Union[Unset, FocusRunFailureReason]):
        detail (Union[Unset, str]):
    """

    reason: Union[Unset, FocusRunFailureReason] = UNSET
    detail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        detail = self.detail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, FocusRunFailureReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_focus_run_failure_reason(_reason)

        detail = d.pop("detail", UNSET)

        focus_run_failure = cls(
            reason=reason,
            detail=detail,
        )

        focus_run_failure.additional_properties = d
        return focus_run_failure

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
