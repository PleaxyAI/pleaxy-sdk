from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.self_approval_record_basis import (
    SelfApprovalRecordBasis,
    check_self_approval_record_basis,
)
from ..models.self_approval_record_waived_exclusion import (
    SelfApprovalRecordWaivedExclusion,
    check_self_approval_record_waived_exclusion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SelfApprovalRecord")


@_attrs_define
class SelfApprovalRecord:
    """
    Attributes:
        basis (Union[Unset, SelfApprovalRecordBasis]):
        eligible_approver_count (Union[Unset, float]):
        evaluated_at (Union[Unset, str]):
        waived_exclusion (Union[Unset, SelfApprovalRecordWaivedExclusion]):
    """

    basis: Union[Unset, SelfApprovalRecordBasis] = UNSET
    eligible_approver_count: Union[Unset, float] = UNSET
    evaluated_at: Union[Unset, str] = UNSET
    waived_exclusion: Union[Unset, SelfApprovalRecordWaivedExclusion] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        basis: Union[Unset, str] = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis

        eligible_approver_count = self.eligible_approver_count

        evaluated_at = self.evaluated_at

        waived_exclusion: Union[Unset, str] = UNSET
        if not isinstance(self.waived_exclusion, Unset):
            waived_exclusion = self.waived_exclusion

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basis is not UNSET:
            field_dict["basis"] = basis
        if eligible_approver_count is not UNSET:
            field_dict["eligibleApproverCount"] = eligible_approver_count
        if evaluated_at is not UNSET:
            field_dict["evaluatedAt"] = evaluated_at
        if waived_exclusion is not UNSET:
            field_dict["waivedExclusion"] = waived_exclusion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _basis = d.pop("basis", UNSET)
        basis: Union[Unset, SelfApprovalRecordBasis]
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_self_approval_record_basis(_basis)

        eligible_approver_count = d.pop("eligibleApproverCount", UNSET)

        evaluated_at = d.pop("evaluatedAt", UNSET)

        _waived_exclusion = d.pop("waivedExclusion", UNSET)
        waived_exclusion: Union[Unset, SelfApprovalRecordWaivedExclusion]
        if isinstance(_waived_exclusion, Unset):
            waived_exclusion = UNSET
        else:
            waived_exclusion = check_self_approval_record_waived_exclusion(
                _waived_exclusion
            )

        self_approval_record = cls(
            basis=basis,
            eligible_approver_count=eligible_approver_count,
            evaluated_at=evaluated_at,
            waived_exclusion=waived_exclusion,
        )

        self_approval_record.additional_properties = d
        return self_approval_record

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
