from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DraftAiOrdersInput")


@_attrs_define
class DraftAiOrdersInput:
    """
    Attributes:
        invoicer_ids (List[str]): The invoicers (cloud accounts or AI provider connections) to draft an order for: the
            ones recommendations lists under uncovered.
        period (Union[Unset, str]): The month the orders cover, YYYY-MM. Default this month.
    """

    invoicer_ids: List[str]
    period: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_ids = self.invoicer_ids

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoicerIds": invoicer_ids,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_ids = cast(List[str], d.pop("invoicerIds"))

        period = d.pop("period", UNSET)

        draft_ai_orders_input = cls(
            invoicer_ids=invoicer_ids,
            period=period,
        )

        draft_ai_orders_input.additional_properties = d
        return draft_ai_orders_input

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
