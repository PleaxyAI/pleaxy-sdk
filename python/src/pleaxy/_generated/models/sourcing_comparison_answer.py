from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingComparisonAnswer")


@_attrs_define
class SourcingComparisonAnswer:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        asked (Union[Unset, bool]):
        file_name (Union[Unset, str]):
        points (Union[None, Unset, float]):
        flagged (Union[Unset, bool]):
        file_id (Union[Unset, str]):
        text_answer (Union[Unset, str]):
        selected_option_ids (Union[Unset, List[str]]):
    """

    supplier_key: Union[Unset, str] = UNSET
    asked: Union[Unset, bool] = UNSET
    file_name: Union[Unset, str] = UNSET
    points: Union[None, Unset, float] = UNSET
    flagged: Union[Unset, bool] = UNSET
    file_id: Union[Unset, str] = UNSET
    text_answer: Union[Unset, str] = UNSET
    selected_option_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        asked = self.asked

        file_name = self.file_name

        points: Union[None, Unset, float]
        if isinstance(self.points, Unset):
            points = UNSET
        else:
            points = self.points

        flagged = self.flagged

        file_id = self.file_id

        text_answer = self.text_answer

        selected_option_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if asked is not UNSET:
            field_dict["asked"] = asked
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if points is not UNSET:
            field_dict["points"] = points
        if flagged is not UNSET:
            field_dict["flagged"] = flagged
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if text_answer is not UNSET:
            field_dict["textAnswer"] = text_answer
        if selected_option_ids is not UNSET:
            field_dict["selectedOptionIds"] = selected_option_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        asked = d.pop("asked", UNSET)

        file_name = d.pop("fileName", UNSET)

        def _parse_points(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        points = _parse_points(d.pop("points", UNSET))

        flagged = d.pop("flagged", UNSET)

        file_id = d.pop("fileId", UNSET)

        text_answer = d.pop("textAnswer", UNSET)

        selected_option_ids = cast(List[str], d.pop("selectedOptionIds", UNSET))

        sourcing_comparison_answer = cls(
            supplier_key=supplier_key,
            asked=asked,
            file_name=file_name,
            points=points,
            flagged=flagged,
            file_id=file_id,
            text_answer=text_answer,
            selected_option_ids=selected_option_ids,
        )

        sourcing_comparison_answer.additional_properties = d
        return sourcing_comparison_answer

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
