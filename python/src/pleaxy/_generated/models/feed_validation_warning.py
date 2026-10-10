from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feed_validation_warning_code import (
    FeedValidationWarningCode,
    check_feed_validation_warning_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedValidationWarning")


@_attrs_define
class FeedValidationWarning:
    """
    Attributes:
        code (Union[Unset, FeedValidationWarningCode]):
        message (Union[Unset, str]):
    """

    code: Union[Unset, FeedValidationWarningCode] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, FeedValidationWarningCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_feed_validation_warning_code(_code)

        message = d.pop("message", UNSET)

        feed_validation_warning = cls(
            code=code,
            message=message,
        )

        feed_validation_warning.additional_properties = d
        return feed_validation_warning

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
