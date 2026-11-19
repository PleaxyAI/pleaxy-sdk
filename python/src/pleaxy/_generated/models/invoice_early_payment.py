from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceEarlyPayment")


@_attrs_define
class InvoiceEarlyPayment:
    """
    Attributes:
        percent (Union[Unset, float]):
        deadline (Union[Unset, str]):
        contract_id (Union[Unset, str]):
    """

    percent: Union[Unset, float] = UNSET
    deadline: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        deadline = self.deadline

        contract_id = self.contract_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        deadline = d.pop("deadline", UNSET)

        contract_id = d.pop("contractId", UNSET)

        invoice_early_payment = cls(
            percent=percent,
            deadline=deadline,
            contract_id=contract_id,
        )

        invoice_early_payment.additional_properties = d
        return invoice_early_payment

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
