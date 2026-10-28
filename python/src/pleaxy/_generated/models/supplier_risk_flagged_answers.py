from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_risk_flagged_answers_state import (
    SupplierRiskFlaggedAnswersState,
    check_supplier_risk_flagged_answers_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierRiskFlaggedAnswers")


@_attrs_define
class SupplierRiskFlaggedAnswers:
    """
    Attributes:
        state (Union[Unset, SupplierRiskFlaggedAnswersState]):
        count (Union[Unset, float]):
    """

    state: Union[Unset, SupplierRiskFlaggedAnswersState] = UNSET
    count: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, SupplierRiskFlaggedAnswersState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_supplier_risk_flagged_answers_state(_state)

        count = d.pop("count", UNSET)

        supplier_risk_flagged_answers = cls(
            state=state,
            count=count,
        )

        supplier_risk_flagged_answers.additional_properties = d
        return supplier_risk_flagged_answers

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
