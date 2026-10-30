from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiAttributionResponseUnmatchedValuesItem")


@_attrs_define
class AiAttributionResponseUnmatchedValuesItem:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        key (Union[Unset, str]):
        value (Union[Unset, str]):
        currency (Union[Unset, str]):
        amount (Union[Unset, float]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        key = self.key

        value = self.value

        currency = self.currency

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        ai_attribution_response_unmatched_values_item = cls(
            invoicer_id=invoicer_id,
            key=key,
            value=value,
            currency=currency,
            amount=amount,
        )

        ai_attribution_response_unmatched_values_item.additional_properties = d
        return ai_attribution_response_unmatched_values_item

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
