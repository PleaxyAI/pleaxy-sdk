from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_attribution_rule_input_dimension import (
    AiAttributionRuleInputDimension,
    check_ai_attribution_rule_input_dimension,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiAttributionRuleInput")


@_attrs_define
class AiAttributionRuleInput:
    """
    Attributes:
        dimension (AiAttributionRuleInputDimension):
        value (str): The value the line must carry for the dimension (and key).
        cost_center (str): The cost center's code.
        id (Union[Unset, str]): The rule's id, to keep it; a new rule gets one.
        invoicer_id (Union[Unset, str]): Only this invoicer's lines (a cloud connection or AI provider id). Every
            invoicer when left out.
        key (Union[Unset, str]): The tag or label key; tag and label only.
    """

    dimension: AiAttributionRuleInputDimension
    value: str
    cost_center: str
    id: Union[Unset, str] = UNSET
    invoicer_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dimension: str = self.dimension

        value = self.value

        cost_center = self.cost_center

        id = self.id

        invoicer_id = self.invoicer_id

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimension": dimension,
                "value": value,
                "costCenter": cost_center,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dimension = check_ai_attribution_rule_input_dimension(d.pop("dimension"))

        value = d.pop("value")

        cost_center = d.pop("costCenter")

        id = d.pop("id", UNSET)

        invoicer_id = d.pop("invoicerId", UNSET)

        key = d.pop("key", UNSET)

        ai_attribution_rule_input = cls(
            dimension=dimension,
            value=value,
            cost_center=cost_center,
            id=id,
            invoicer_id=invoicer_id,
            key=key,
        )

        ai_attribution_rule_input.additional_properties = d
        return ai_attribution_rule_input

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
