from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_answer_input import FileAnswerInput


T = TypeVar("T", bound="PurchaseRequestAnswerInput")


@_attrs_define
class PurchaseRequestAnswerInput:
    """
    Attributes:
        field_id (str): QuestionnaireFieldDef.id of a kind === 'custom' field
        text_answer (Union[Unset, str]): text, long_text, number (e.g. "1250.5") and date (YYYY-MM-DD) questions
        selected_option_ids (Union[Unset, List[str]]): yes_no ("yes"/"no"), single_choice and multi_choice questions -
            option ids
        file (Union[Unset, FileAnswerInput]):
    """

    field_id: str
    text_answer: Union[Unset, str] = UNSET
    selected_option_ids: Union[Unset, List[str]] = UNSET
    file: Union[Unset, "FileAnswerInput"] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldId": field_id,
            }
        )
        if text_answer is not UNSET:
            field_dict["textAnswer"] = text_answer
        if selected_option_ids is not UNSET:
            field_dict["selectedOptionIds"] = selected_option_ids
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_answer_input import FileAnswerInput

        d = src_dict.copy()
        field_id = d.pop("fieldId")

        text_answer = d.pop("textAnswer", UNSET)

        selected_option_ids = cast(List[str], d.pop("selectedOptionIds", UNSET))

        _file = d.pop("file", UNSET)
        file: Union[Unset, FileAnswerInput]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileAnswerInput.from_dict(_file)

        purchase_request_answer_input = cls(
            field_id=field_id,
            text_answer=text_answer,
            selected_option_ids=selected_option_ids,
            file=file,
        )

        purchase_request_answer_input.additional_properties = d
        return purchase_request_answer_input

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
