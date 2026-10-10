from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spend_limit_breach_subject import (
    SpendLimitBreachSubject,
    check_spend_limit_breach_subject,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_fx import ApprovalFx


T = TypeVar("T", bound="SpendLimitBreach")


@_attrs_define
class SpendLimitBreach:
    """
    Attributes:
        employee_key (Union[Unset, str]):
        employee_name (Union[Unset, str]):
        limit_amount (Union[Unset, float]):
        limit_currency (Union[Unset, str]):
        fx (Union[Unset, ApprovalFx]):
        subject (Union[Unset, SpendLimitBreachSubject]):
        applied (Union[Unset, bool]):
    """

    employee_key: Union[Unset, str] = UNSET
    employee_name: Union[Unset, str] = UNSET
    limit_amount: Union[Unset, float] = UNSET
    limit_currency: Union[Unset, str] = UNSET
    fx: Union[Unset, "ApprovalFx"] = UNSET
    subject: Union[Unset, SpendLimitBreachSubject] = UNSET
    applied: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_key = self.employee_key

        employee_name = self.employee_name

        limit_amount = self.limit_amount

        limit_currency = self.limit_currency

        fx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fx, Unset):
            fx = self.fx.to_dict()

        subject: Union[Unset, str] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject

        applied = self.applied

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_key is not UNSET:
            field_dict["employeeKey"] = employee_key
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if limit_amount is not UNSET:
            field_dict["limitAmount"] = limit_amount
        if limit_currency is not UNSET:
            field_dict["limitCurrency"] = limit_currency
        if fx is not UNSET:
            field_dict["fx"] = fx
        if subject is not UNSET:
            field_dict["subject"] = subject
        if applied is not UNSET:
            field_dict["applied"] = applied

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_fx import ApprovalFx

        d = src_dict.copy()
        employee_key = d.pop("employeeKey", UNSET)

        employee_name = d.pop("employeeName", UNSET)

        limit_amount = d.pop("limitAmount", UNSET)

        limit_currency = d.pop("limitCurrency", UNSET)

        _fx = d.pop("fx", UNSET)
        fx: Union[Unset, ApprovalFx]
        if isinstance(_fx, Unset):
            fx = UNSET
        else:
            fx = ApprovalFx.from_dict(_fx)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, SpendLimitBreachSubject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = check_spend_limit_breach_subject(_subject)

        applied = d.pop("applied", UNSET)

        spend_limit_breach = cls(
            employee_key=employee_key,
            employee_name=employee_name,
            limit_amount=limit_amount,
            limit_currency=limit_currency,
            fx=fx,
            subject=subject,
            applied=applied,
        )

        spend_limit_breach.additional_properties = d
        return spend_limit_breach

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
