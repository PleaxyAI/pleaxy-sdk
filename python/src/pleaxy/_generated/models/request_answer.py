from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.questionnaire_file_answer import QuestionnaireFileAnswer


T = TypeVar("T", bound="RequestAnswer")


@_attrs_define
class RequestAnswer:
    """
    Attributes:
        field_id (Union[Unset, str]):
        text_answer (Union[Unset, str]):
        selected_option_ids (Union[Unset, List[str]]):
        file (Union[Unset, QuestionnaireFileAnswer]):
        flagged (Union[Unset, bool]):
    """

    field_id: Union[Unset, str] = UNSET
    text_answer: Union[Unset, str] = UNSET
    selected_option_ids: Union[Unset, List[str]] = UNSET
    file: Union[Unset, "QuestionnaireFileAnswer"] = UNSET
    flagged: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_id = self.field_id

        text_answer = self.text_answer

        selected_option_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        flagged = self.flagged

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if text_answer is not UNSET:
            field_dict["textAnswer"] = text_answer
        if selected_option_ids is not UNSET:
            field_dict["selectedOptionIds"] = selected_option_ids
        if file is not UNSET:
            field_dict["file"] = file
        if flagged is not UNSET:
            field_dict["flagged"] = flagged

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.questionnaire_file_answer import QuestionnaireFileAnswer

        d = src_dict.copy()
        field_id = d.pop("fieldId", UNSET)

        text_answer = d.pop("textAnswer", UNSET)

        selected_option_ids = cast(List[str], d.pop("selectedOptionIds", UNSET))

        _file = d.pop("file", UNSET)
        file: Union[Unset, QuestionnaireFileAnswer]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = QuestionnaireFileAnswer.from_dict(_file)

        flagged = d.pop("flagged", UNSET)

        request_answer = cls(
            field_id=field_id,
            text_answer=text_answer,
            selected_option_ids=selected_option_ids,
            file=file,
            flagged=flagged,
        )

        request_answer.additional_properties = d
        return request_answer

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
