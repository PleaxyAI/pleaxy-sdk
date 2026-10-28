from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_risk_bank_state import (
    SupplierRiskBankState,
    check_supplier_risk_bank_state,
)
from ..models.supplier_risk_bank_status import (
    SupplierRiskBankStatus,
    check_supplier_risk_bank_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierRiskBank")


@_attrs_define
class SupplierRiskBank:
    """
    Attributes:
        state (Union[Unset, SupplierRiskBankState]):
        waiting (Union[Unset, float]):
        status (Union[Unset, SupplierRiskBankStatus]):
    """

    state: Union[Unset, SupplierRiskBankState] = UNSET
    waiting: Union[Unset, float] = UNSET
    status: Union[Unset, SupplierRiskBankStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        waiting = self.waiting

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if waiting is not UNSET:
            field_dict["waiting"] = waiting
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, SupplierRiskBankState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_supplier_risk_bank_state(_state)

        waiting = d.pop("waiting", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierRiskBankStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_risk_bank_status(_status)

        supplier_risk_bank = cls(
            state=state,
            waiting=waiting,
            status=status,
        )

        supplier_risk_bank.additional_properties = d
        return supplier_risk_bank

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
