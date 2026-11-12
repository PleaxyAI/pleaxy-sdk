from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingQuestionAnswer")


@_attrs_define
class SourcingQuestionAnswer:
    """
    Attributes:
        field_id (Union[Unset, str]):
        text_answer (Union[Unset, str]):
        selected_option_ids (Union[Unset, List[str]]):
        file_id (Union[Unset, str]):
    """

    field_id: Union[Unset, str] = UNSET
    text_answer: Union[Unset, str] = UNSET
    selected_option_ids: Union[Unset, List[str]] = UNSET
    file_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        text_answer = self.text_answer

        selected_option_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        file_id = self.file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if text_answer is not UNSET:
            field_dict["textAnswer"] = text_answer
        if selected_option_ids is not UNSET:
            field_dict["selectedOptionIds"] = selected_option_ids
        if file_id is not UNSET:
            field_dict["fileId"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_id = d.pop("fieldId", UNSET)

        text_answer = d.pop("textAnswer", UNSET)

        selected_option_ids = cast(List[str], d.pop("selectedOptionIds", UNSET))

        file_id = d.pop("fileId", UNSET)

        sourcing_question_answer = cls(
            field_id=field_id,
            text_answer=text_answer,
            selected_option_ids=selected_option_ids,
            file_id=file_id,
        )

        sourcing_question_answer.additional_properties = d
        return sourcing_question_answer

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
