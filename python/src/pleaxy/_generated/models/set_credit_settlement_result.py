from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_credit_settlement_result_credit_settlement import (
    SetCreditSettlementResultCreditSettlement,
    check_set_credit_settlement_result_credit_settlement,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetCreditSettlementResult")


@_attrs_define
class SetCreditSettlementResult:
    """
    Attributes:
        credit_settlement (Union[Unset, SetCreditSettlementResultCreditSettlement]):
        chosen (Union[Unset, bool]):
    """

    credit_settlement: Union[Unset, SetCreditSettlementResultCreditSettlement] = UNSET
    chosen: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_settlement: Union[Unset, str] = UNSET
        if not isinstance(self.credit_settlement, Unset):
            credit_settlement = self.credit_settlement

        chosen = self.chosen

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_settlement is not UNSET:
            field_dict["creditSettlement"] = credit_settlement
        if chosen is not UNSET:
            field_dict["chosen"] = chosen

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _credit_settlement = d.pop("creditSettlement", UNSET)
        credit_settlement: Union[Unset, SetCreditSettlementResultCreditSettlement]
        if isinstance(_credit_settlement, Unset):
            credit_settlement = UNSET
        else:
            credit_settlement = check_set_credit_settlement_result_credit_settlement(
                _credit_settlement
            )

        chosen = d.pop("chosen", UNSET)

        set_credit_settlement_result = cls(
            credit_settlement=credit_settlement,
            chosen=chosen,
        )

        set_credit_settlement_result.additional_properties = d
        return set_credit_settlement_result

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
