from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_reconciliation_result_ucp import (
        GetInvoiceReconciliationResultUcp,
    )
    from ..models.reconciliation_result import ReconciliationResult


T = TypeVar("T", bound="GetInvoiceReconciliationResult")


@_attrs_define
class GetInvoiceReconciliationResult:
    """
    Attributes:
        ucp (Union[Unset, GetInvoiceReconciliationResultUcp]):
        reconciliation (Union[Unset, ReconciliationResult]):
    """

    ucp: Union[Unset, "GetInvoiceReconciliationResultUcp"] = UNSET
    reconciliation: Union[Unset, "ReconciliationResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ucp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ucp, Unset):
            ucp = self.ucp.to_dict()

        reconciliation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reconciliation, Unset):
            reconciliation = self.reconciliation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ucp is not UNSET:
            field_dict["ucp"] = ucp
        if reconciliation is not UNSET:
            field_dict["reconciliation"] = reconciliation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_invoice_reconciliation_result_ucp import (
            GetInvoiceReconciliationResultUcp,
        )
        from ..models.reconciliation_result import ReconciliationResult

        d = src_dict.copy()
        _ucp = d.pop("ucp", UNSET)
        ucp: Union[Unset, GetInvoiceReconciliationResultUcp]
        if isinstance(_ucp, Unset):
            ucp = UNSET
        else:
            ucp = GetInvoiceReconciliationResultUcp.from_dict(_ucp)

        _reconciliation = d.pop("reconciliation", UNSET)
        reconciliation: Union[Unset, ReconciliationResult]
        if isinstance(_reconciliation, Unset):
            reconciliation = UNSET
        else:
            reconciliation = ReconciliationResult.from_dict(_reconciliation)

        get_invoice_reconciliation_result = cls(
            ucp=ucp,
            reconciliation=reconciliation,
        )

        get_invoice_reconciliation_result.additional_properties = d
        return get_invoice_reconciliation_result

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
