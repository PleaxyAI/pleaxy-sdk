from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckAiSpendInput")


@_attrs_define
class CheckAiSpendInput:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        po_id (Union[Unset, str]):
        period (Union[Unset, str]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    po_id: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        cost_center = self.cost_center

        po_id = self.po_id

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        po_id = d.pop("poId", UNSET)

        period = d.pop("period", UNSET)

        check_ai_spend_input = cls(
            invoicer_id=invoicer_id,
            cost_center=cost_center,
            po_id=po_id,
            period=period,
        )

        check_ai_spend_input.additional_properties = d
        return check_ai_spend_input

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
