from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuestionCondition")


@_attrs_define
class QuestionCondition:
    """
    Attributes:
        field_id (Union[Unset, str]):
        any_of (Union[Unset, List[str]]):
    """

    field_id: Union[Unset, str] = UNSET
    any_of: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        any_of: Union[Unset, List[str]] = UNSET
        if not isinstance(self.any_of, Unset):
            any_of = self.any_of

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("fieldId", UNSET)

        any_of = cast(List[str], d.pop("anyOf", UNSET))

        question_condition = cls(
            field_id=field_id,
            any_of=any_of,
        )

        question_condition.additional_properties = d
        return question_condition

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
