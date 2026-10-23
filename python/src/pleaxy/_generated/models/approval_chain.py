from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_chain_status import (
    ApprovalChainStatus,
    check_approval_chain_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain_from_request import ApprovalChainFromRequest
    from ..models.approval_fx import ApprovalFx
    from ..models.approval_history_entry import ApprovalHistoryEntry
    from ..models.approval_stage_group_instance import ApprovalStageGroupInstance
    from ..models.spend_limit_gate import SpendLimitGate


T = TypeVar("T", bound="ApprovalChain")


@_attrs_define
class ApprovalChain:
    """
    Attributes:
        requester (Union[Unset, str]):
        requester_employee_key (Union[Unset, str]):
        groups (Union[Unset, List['ApprovalStageGroupInstance']]):
        group_index (Union[Unset, float]):
        status (Union[Unset, ApprovalChainStatus]):
        history (Union[Unset, List['ApprovalHistoryEntry']]):
        autonomy (Union[Unset, bool]):
        spend_limit_gate (Union[Unset, SpendLimitGate]):
        excluded_employee_keys (Union[Unset, List[str]]):
        self_approved (Union[Unset, bool]):
        fx (Union[Unset, ApprovalFx]):
        from_request (Union[Unset, ApprovalChainFromRequest]):
    """

    requester: Union[Unset, str] = UNSET
    requester_employee_key: Union[Unset, str] = UNSET
    groups: Union[Unset, List["ApprovalStageGroupInstance"]] = UNSET
    group_index: Union[Unset, float] = UNSET
    status: Union[Unset, ApprovalChainStatus] = UNSET
    history: Union[Unset, List["ApprovalHistoryEntry"]] = UNSET
    autonomy: Union[Unset, bool] = UNSET
    spend_limit_gate: Union[Unset, "SpendLimitGate"] = UNSET
    excluded_employee_keys: Union[Unset, List[str]] = UNSET
    self_approved: Union[Unset, bool] = UNSET
    fx: Union[Unset, "ApprovalFx"] = UNSET
    from_request: Union[Unset, "ApprovalChainFromRequest"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requester = self.requester

        requester_employee_key = self.requester_employee_key

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        group_index = self.group_index

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        autonomy = self.autonomy

        spend_limit_gate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spend_limit_gate, Unset):
            spend_limit_gate = self.spend_limit_gate.to_dict()

        excluded_employee_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_employee_keys, Unset):
            excluded_employee_keys = self.excluded_employee_keys

        self_approved = self.self_approved

        fx: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fx, Unset):
            fx = self.fx.to_dict()

        from_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_request, Unset):
            from_request = self.from_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requester is not UNSET:
            field_dict["requester"] = requester
        if requester_employee_key is not UNSET:
            field_dict["requesterEmployeeKey"] = requester_employee_key
        if groups is not UNSET:
            field_dict["groups"] = groups
        if group_index is not UNSET:
            field_dict["groupIndex"] = group_index
        if status is not UNSET:
            field_dict["status"] = status
        if history is not UNSET:
            field_dict["history"] = history
        if autonomy is not UNSET:
            field_dict["autonomy"] = autonomy
        if spend_limit_gate is not UNSET:
            field_dict["spendLimitGate"] = spend_limit_gate
        if excluded_employee_keys is not UNSET:
            field_dict["excludedEmployeeKeys"] = excluded_employee_keys
        if self_approved is not UNSET:
            field_dict["selfApproved"] = self_approved
        if fx is not UNSET:
            field_dict["fx"] = fx
        if from_request is not UNSET:
            field_dict["fromRequest"] = from_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain_from_request import ApprovalChainFromRequest
        from ..models.approval_fx import ApprovalFx
        from ..models.approval_history_entry import ApprovalHistoryEntry
        from ..models.approval_stage_group_instance import ApprovalStageGroupInstance
        from ..models.spend_limit_gate import SpendLimitGate

        d = src_dict.copy()
        requester = d.pop("requester", UNSET)

        requester_employee_key = d.pop("requesterEmployeeKey", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ApprovalStageGroupInstance.from_dict(groups_item_data)

            groups.append(groups_item)

        group_index = d.pop("groupIndex", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApprovalChainStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_approval_chain_status(_status)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = ApprovalHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        autonomy = d.pop("autonomy", UNSET)

        _spend_limit_gate = d.pop("spendLimitGate", UNSET)
        spend_limit_gate: Union[Unset, SpendLimitGate]
        if isinstance(_spend_limit_gate, Unset):
            spend_limit_gate = UNSET
        else:
            spend_limit_gate = SpendLimitGate.from_dict(_spend_limit_gate)

        excluded_employee_keys = cast(List[str], d.pop("excludedEmployeeKeys", UNSET))

        self_approved = d.pop("selfApproved", UNSET)

        _fx = d.pop("fx", UNSET)
        fx: Union[Unset, ApprovalFx]
        if isinstance(_fx, Unset):
            fx = UNSET
        else:
            fx = ApprovalFx.from_dict(_fx)

        _from_request = d.pop("fromRequest", UNSET)
        from_request: Union[Unset, ApprovalChainFromRequest]
        if isinstance(_from_request, Unset):
            from_request = UNSET
        else:
            from_request = ApprovalChainFromRequest.from_dict(_from_request)

        approval_chain = cls(
            requester=requester,
            requester_employee_key=requester_employee_key,
            groups=groups,
            group_index=group_index,
            status=status,
            history=history,
            autonomy=autonomy,
            spend_limit_gate=spend_limit_gate,
            excluded_employee_keys=excluded_employee_keys,
            self_approved=self_approved,
            fx=fx,
            from_request=from_request,
        )

        approval_chain.additional_properties = d
        return approval_chain

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
