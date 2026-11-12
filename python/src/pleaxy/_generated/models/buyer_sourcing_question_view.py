from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerSourcingQuestionView")


@_attrs_define
class BuyerSourcingQuestionView:
    """
    Attributes:
        id (str):
        supplier_key (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        text (Union[Unset, str]):
        asked_at (Union[Unset, str]):
        answer (Union[Unset, str]):
        answered_at (Union[Unset, str]):
    """

    id: str
    supplier_key: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    asked_at: Union[Unset, str] = UNSET
    answer: Union[Unset, str] = UNSET
    answered_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        supplier_key = self.supplier_key

        supplier_name = self.supplier_name

        text = self.text

        asked_at = self.asked_at

        answer = self.answer

        answered_at = self.answered_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if text is not UNSET:
            field_dict["text"] = text
        if asked_at is not UNSET:
            field_dict["askedAt"] = asked_at
        if answer is not UNSET:
            field_dict["answer"] = answer
        if answered_at is not UNSET:
            field_dict["answeredAt"] = answered_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        supplier_key = d.pop("supplierKey", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        text = d.pop("text", UNSET)

        asked_at = d.pop("askedAt", UNSET)

        answer = d.pop("answer", UNSET)

        answered_at = d.pop("answeredAt", UNSET)

        buyer_sourcing_question_view = cls(
            id=id,
            supplier_key=supplier_key,
            supplier_name=supplier_name,
            text=text,
            asked_at=asked_at,
            answer=answer,
            answered_at=answered_at,
        )

        buyer_sourcing_question_view.additional_properties = d
        return buyer_sourcing_question_view

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
