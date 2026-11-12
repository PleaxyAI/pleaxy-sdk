from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_read_sentence import AssistantReadSentence


T = TypeVar("T", bound="SourcingAssistantRead")


@_attrs_define
class SourcingAssistantRead:
    """
    Attributes:
        sentences (Union[Unset, List['AssistantReadSentence']]):
        model (Union[Unset, str]):
        generated_at (Union[Unset, str]):
        input_hash (Union[Unset, str]):
    """

    sentences: Union[Unset, List["AssistantReadSentence"]] = UNSET
    model: Union[Unset, str] = UNSET
    generated_at: Union[Unset, str] = UNSET
    input_hash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sentences: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sentences, Unset):
            sentences = []
            for sentences_item_data in self.sentences:
                sentences_item = sentences_item_data.to_dict()
                sentences.append(sentences_item)

        model = self.model

        generated_at = self.generated_at

        input_hash = self.input_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sentences is not UNSET:
            field_dict["sentences"] = sentences
        if model is not UNSET:
            field_dict["model"] = model
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at
        if input_hash is not UNSET:
            field_dict["inputHash"] = input_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assistant_read_sentence import AssistantReadSentence

        d = src_dict.copy()
        sentences = []
        _sentences = d.pop("sentences", UNSET)
        for sentences_item_data in _sentences or []:
            sentences_item = AssistantReadSentence.from_dict(sentences_item_data)

            sentences.append(sentences_item)

        model = d.pop("model", UNSET)

        generated_at = d.pop("generatedAt", UNSET)

        input_hash = d.pop("inputHash", UNSET)

        sourcing_assistant_read = cls(
            sentences=sentences,
            model=model,
            generated_at=generated_at,
            input_hash=input_hash,
        )

        sourcing_assistant_read.additional_properties = d
        return sourcing_assistant_read

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
