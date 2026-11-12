from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_settlement_input_credit_settlement import (
    CreditSettlementInputCreditSettlement,
    check_credit_settlement_input_credit_settlement,
)

T = TypeVar("T", bound="CreditSettlementInput")


@_attrs_define
class CreditSettlementInput:
    """
    Attributes:
        credit_settlement (CreditSettlementInputCreditSettlement): pleaxy: accepted credits are applied to invoices
            here. accounting_system: they go out in the payment export for your ERP to clear.
    """

    credit_settlement: CreditSettlementInputCreditSettlement
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_settlement: str = self.credit_settlement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creditSettlement": credit_settlement,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_settlement = check_credit_settlement_input_credit_settlement(
            d.pop("creditSettlement")
        )

        credit_settlement_input = cls(
            credit_settlement=credit_settlement,
        )

        credit_settlement_input.additional_properties = d
        return credit_settlement_input

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
