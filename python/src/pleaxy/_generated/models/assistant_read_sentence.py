from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_read_cite import AssistantReadCite


T = TypeVar("T", bound="AssistantReadSentence")


@_attrs_define
class AssistantReadSentence:
    """
    Attributes:
        text (Union[Unset, str]):
        cites (Union[Unset, List['AssistantReadCite']]):
    """

    text: Union[Unset, str] = UNSET
    cites: Union[Unset, List["AssistantReadCite"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        cites: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cites, Unset):
            cites = []
            for cites_item_data in self.cites:
                cites_item = cites_item_data.to_dict()
                cites.append(cites_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if cites is not UNSET:
            field_dict["cites"] = cites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assistant_read_cite import AssistantReadCite

        d = src_dict.copy()
        text = d.pop("text", UNSET)

        cites = []
        _cites = d.pop("cites", UNSET)
        for cites_item_data in _cites or []:
            cites_item = AssistantReadCite.from_dict(cites_item_data)

            cites.append(cites_item)

        assistant_read_sentence = cls(
            text=text,
            cites=cites,
        )

        assistant_read_sentence.additional_properties = d
        return assistant_read_sentence

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
