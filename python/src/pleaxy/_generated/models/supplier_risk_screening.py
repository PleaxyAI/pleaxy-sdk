from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_risk_screening_state import (
    SupplierRiskScreeningState,
    check_supplier_risk_screening_state,
)
from ..models.supplier_risk_screening_status import (
    SupplierRiskScreeningStatus,
    check_supplier_risk_screening_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierRiskScreening")


@_attrs_define
class SupplierRiskScreening:
    """
    Attributes:
        state (Union[Unset, SupplierRiskScreeningState]):
        status (Union[Unset, SupplierRiskScreeningStatus]):
        checked_at (Union[Unset, str]):
    """

    state: Union[Unset, SupplierRiskScreeningState] = UNSET
    status: Union[Unset, SupplierRiskScreeningStatus] = UNSET
    checked_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        checked_at = self.checked_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, SupplierRiskScreeningState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_supplier_risk_screening_state(_state)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierRiskScreeningStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_risk_screening_status(_status)

        checked_at = d.pop("checkedAt", UNSET)

        supplier_risk_screening = cls(
            state=state,
            status=status,
            checked_at=checked_at,
        )

        supplier_risk_screening.additional_properties = d
        return supplier_risk_screening

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
