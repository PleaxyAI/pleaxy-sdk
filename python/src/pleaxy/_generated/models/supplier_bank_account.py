from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_account_status import (
    SupplierBankAccountStatus,
    check_supplier_bank_account_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remittance_instructions import RemittanceInstructions
    from ..models.supplier_bank_account_approval import SupplierBankAccountApproval
    from ..models.supplier_bank_account_history_entry import (
        SupplierBankAccountHistoryEntry,
    )
    from ..models.supplier_bank_account_learned_from import (
        SupplierBankAccountLearnedFrom,
    )
    from ..models.supplier_bank_account_pending_change import (
        SupplierBankAccountPendingChange,
    )


T = TypeVar("T", bound="SupplierBankAccount")


@_attrs_define
class SupplierBankAccount:
    """
    Attributes:
        id (str):
        supplier_key (Union[Unset, str]):
        lane_key (Union[Unset, str]):
        payee_name (Union[Unset, str]):
        currency (Union[Unset, str]):
        details (Union[Unset, RemittanceInstructions]):
        status (Union[Unset, SupplierBankAccountStatus]):
        learned_from (Union[Unset, SupplierBankAccountLearnedFrom]):
        approval (Union[Unset, SupplierBankAccountApproval]):
        pending_change (Union[Unset, SupplierBankAccountPendingChange]):
        history (Union[Unset, List['SupplierBankAccountHistoryEntry']]):
        version (Union[Unset, float]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    id: str
    supplier_key: Union[Unset, str] = UNSET
    lane_key: Union[Unset, str] = UNSET
    payee_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    details: Union[Unset, "RemittanceInstructions"] = UNSET
    status: Union[Unset, SupplierBankAccountStatus] = UNSET
    learned_from: Union[Unset, "SupplierBankAccountLearnedFrom"] = UNSET
    approval: Union[Unset, "SupplierBankAccountApproval"] = UNSET
    pending_change: Union[Unset, "SupplierBankAccountPendingChange"] = UNSET
    history: Union[Unset, List["SupplierBankAccountHistoryEntry"]] = UNSET
    version: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        supplier_key = self.supplier_key

        lane_key = self.lane_key

        payee_name = self.payee_name

        currency = self.currency

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        learned_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.learned_from, Unset):
            learned_from = self.learned_from.to_dict()

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        pending_change: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pending_change, Unset):
            pending_change = self.pending_change.to_dict()

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        version = self.version

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if lane_key is not UNSET:
            field_dict["laneKey"] = lane_key
        if payee_name is not UNSET:
            field_dict["payeeName"] = payee_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if details is not UNSET:
            field_dict["details"] = details
        if status is not UNSET:
            field_dict["status"] = status
        if learned_from is not UNSET:
            field_dict["learnedFrom"] = learned_from
        if approval is not UNSET:
            field_dict["approval"] = approval
        if pending_change is not UNSET:
            field_dict["pendingChange"] = pending_change
        if history is not UNSET:
            field_dict["history"] = history
        if version is not UNSET:
            field_dict["version"] = version
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.remittance_instructions import RemittanceInstructions
        from ..models.supplier_bank_account_approval import SupplierBankAccountApproval
        from ..models.supplier_bank_account_history_entry import (
            SupplierBankAccountHistoryEntry,
        )
        from ..models.supplier_bank_account_learned_from import (
            SupplierBankAccountLearnedFrom,
        )
        from ..models.supplier_bank_account_pending_change import (
            SupplierBankAccountPendingChange,
        )

        d = src_dict.copy()
        id = d.pop("id")

        supplier_key = d.pop("supplierKey", UNSET)

        lane_key = d.pop("laneKey", UNSET)

        payee_name = d.pop("payeeName", UNSET)

        currency = d.pop("currency", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, RemittanceInstructions]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RemittanceInstructions.from_dict(_details)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SupplierBankAccountStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_supplier_bank_account_status(_status)

        _learned_from = d.pop("learnedFrom", UNSET)
        learned_from: Union[Unset, SupplierBankAccountLearnedFrom]
        if isinstance(_learned_from, Unset):
            learned_from = UNSET
        else:
            learned_from = SupplierBankAccountLearnedFrom.from_dict(_learned_from)

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, SupplierBankAccountApproval]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = SupplierBankAccountApproval.from_dict(_approval)

        _pending_change = d.pop("pendingChange", UNSET)
        pending_change: Union[Unset, SupplierBankAccountPendingChange]
        if isinstance(_pending_change, Unset):
            pending_change = UNSET
        else:
            pending_change = SupplierBankAccountPendingChange.from_dict(_pending_change)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = SupplierBankAccountHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        version = d.pop("version", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        supplier_bank_account = cls(
            id=id,
            supplier_key=supplier_key,
            lane_key=lane_key,
            payee_name=payee_name,
            currency=currency,
            details=details,
            status=status,
            learned_from=learned_from,
            approval=approval,
            pending_change=pending_change,
            history=history,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
        )

        supplier_bank_account.additional_properties = d
        return supplier_bank_account

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
