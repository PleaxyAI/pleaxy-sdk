from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_attribution_rule_view_matched_item import (
        AiAttributionRuleViewMatchedItem,
    )


T = TypeVar("T", bound="AiAttributionRuleView")


@_attrs_define
class AiAttributionRuleView:
    """
    Attributes:
        id (str):
        invoicer_id (Union[Unset, str]):
        dimension (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        matched (Union[Unset, List['AiAttributionRuleViewMatchedItem']]):
    """

    id: str
    invoicer_id: Union[Unset, str] = UNSET
    dimension: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    matched: Union[Unset, List["AiAttributionRuleViewMatchedItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        invoicer_id = self.invoicer_id

        dimension = self.dimension

        key = self.key

        value = self.value

        cost_center = self.cost_center

        matched: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matched, Unset):
            matched = []
            for matched_item_data in self.matched:
                matched_item = matched_item_data.to_dict()
                matched.append(matched_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if matched is not UNSET:
            field_dict["matched"] = matched

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_attribution_rule_view_matched_item import (
            AiAttributionRuleViewMatchedItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        invoicer_id = d.pop("invoicerId", UNSET)

        dimension = d.pop("dimension", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        matched = []
        _matched = d.pop("matched", UNSET)
        for matched_item_data in _matched or []:
            matched_item = AiAttributionRuleViewMatchedItem.from_dict(matched_item_data)

            matched.append(matched_item)

        ai_attribution_rule_view = cls(
            id=id,
            invoicer_id=invoicer_id,
            dimension=dimension,
            key=key,
            value=value,
            cost_center=cost_center,
            matched=matched,
        )

        ai_attribution_rule_view.additional_properties = d
        return ai_attribution_rule_view

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
