from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_fx import ApprovalFx
    from ..models.spend_limit_breach import SpendLimitBreach


T = TypeVar("T", bound="SpendLimitGate")


@_attrs_define
class SpendLimitGate:
    """
    Attributes:
        employee_key (Union[Unset, str]):
        employee_name (Union[Unset, str]):
        limit_amount (Union[Unset, float]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        limit_currency (Union[Unset, str]):
        fx (Union[Unset, ApprovalFx]):
        approver_employee_key (Union[Unset, str]):
        approver_name (Union[Unset, str]):
        merged_into_existing_stage (Union[Unset, bool]):
        exceeded (Union[Unset, List['SpendLimitBreach']]):
        satisfied_by_employee_key (Union[Unset, str]):
        satisfied_by_name (Union[Unset, str]):
        gated_at (Union[Unset, str]):
        satisfied_at (Union[Unset, str]):
        satisfied_amount (Union[Unset, float]):
    """

    employee_key: Union[Unset, str] = UNSET
    employee_name: Union[Unset, str] = UNSET
    limit_amount: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    limit_currency: Union[Unset, str] = UNSET
    fx: Union[Unset, "ApprovalFx"] = UNSET
    approver_employee_key: Union[Unset, str] = UNSET
    approver_name: Union[Unset, str] = UNSET
    merged_into_existing_stage: Union[Unset, bool] = UNSET
    exceeded: Union[Unset, List["SpendLimitBreach"]] = UNSET
    satisfied_by_employee_key: Union[Unset, str] = UNSET
    satisfied_by_name: Union[Unset, str] = UNSET
    gated_at: Union[Unset, str] = UNSET
    satisfied_at: Union[Unset, str] = UNSET
    satisfied_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_key = self.employee_key

        employee_name = self.employee_name

        limit_amount = self.limit_amount

        amount = self.amount

        currency = self.currency

        limit_currency = self.limit_currency

        fx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fx, Unset):
            fx = self.fx.to_dict()

        approver_employee_key = self.approver_employee_key

        approver_name = self.approver_name

        merged_into_existing_stage = self.merged_into_existing_stage

        exceeded: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exceeded, Unset):
            exceeded = []
            for exceeded_item_data in self.exceeded:
                exceeded_item = exceeded_item_data.to_dict()
                exceeded.append(exceeded_item)

        satisfied_by_employee_key = self.satisfied_by_employee_key

        satisfied_by_name = self.satisfied_by_name

        gated_at = self.gated_at

        satisfied_at = self.satisfied_at

        satisfied_amount = self.satisfied_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_key is not UNSET:
            field_dict["employeeKey"] = employee_key
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if limit_amount is not UNSET:
            field_dict["limitAmount"] = limit_amount
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if limit_currency is not UNSET:
            field_dict["limitCurrency"] = limit_currency
        if fx is not UNSET:
            field_dict["fx"] = fx
        if approver_employee_key is not UNSET:
            field_dict["approverEmployeeKey"] = approver_employee_key
        if approver_name is not UNSET:
            field_dict["approverName"] = approver_name
        if merged_into_existing_stage is not UNSET:
            field_dict["mergedIntoExistingStage"] = merged_into_existing_stage
        if exceeded is not UNSET:
            field_dict["exceeded"] = exceeded
        if satisfied_by_employee_key is not UNSET:
            field_dict["satisfiedByEmployeeKey"] = satisfied_by_employee_key
        if satisfied_by_name is not UNSET:
            field_dict["satisfiedByName"] = satisfied_by_name
        if gated_at is not UNSET:
            field_dict["gatedAt"] = gated_at
        if satisfied_at is not UNSET:
            field_dict["satisfiedAt"] = satisfied_at
        if satisfied_amount is not UNSET:
            field_dict["satisfiedAmount"] = satisfied_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_fx import ApprovalFx
        from ..models.spend_limit_breach import SpendLimitBreach

        d = src_dict.copy()
        employee_key = d.pop("employeeKey", UNSET)

        employee_name = d.pop("employeeName", UNSET)

        limit_amount = d.pop("limitAmount", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        limit_currency = d.pop("limitCurrency", UNSET)

        _fx = d.pop("fx", UNSET)
        fx: Union[Unset, ApprovalFx]
        if isinstance(_fx, Unset):
            fx = UNSET
        else:
            fx = ApprovalFx.from_dict(_fx)

        approver_employee_key = d.pop("approverEmployeeKey", UNSET)

        approver_name = d.pop("approverName", UNSET)

        merged_into_existing_stage = d.pop("mergedIntoExistingStage", UNSET)

        exceeded = []
        _exceeded = d.pop("exceeded", UNSET)
        for exceeded_item_data in _exceeded or []:
            exceeded_item = SpendLimitBreach.from_dict(exceeded_item_data)

            exceeded.append(exceeded_item)

        satisfied_by_employee_key = d.pop("satisfiedByEmployeeKey", UNSET)

        satisfied_by_name = d.pop("satisfiedByName", UNSET)

        gated_at = d.pop("gatedAt", UNSET)

        satisfied_at = d.pop("satisfiedAt", UNSET)

        satisfied_amount = d.pop("satisfiedAmount", UNSET)

        spend_limit_gate = cls(
            employee_key=employee_key,
            employee_name=employee_name,
            limit_amount=limit_amount,
            amount=amount,
            currency=currency,
            limit_currency=limit_currency,
            fx=fx,
            approver_employee_key=approver_employee_key,
            approver_name=approver_name,
            merged_into_existing_stage=merged_into_existing_stage,
            exceeded=exceeded,
            satisfied_by_employee_key=satisfied_by_employee_key,
            satisfied_by_name=satisfied_by_name,
            gated_at=gated_at,
            satisfied_at=satisfied_at,
            satisfied_amount=satisfied_amount,
        )

        spend_limit_gate.additional_properties = d
        return spend_limit_gate

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
