from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_reconciliation_result_ucp_capabilities_ai_pleaxy_procurement_reconciliation_item import (
        GetInvoiceReconciliationResultUcpCapabilitiesAiPleaxyProcurementReconciliationItem,
    )


T = TypeVar("T", bound="GetInvoiceReconciliationResultUcpCapabilities")


@_attrs_define
class GetInvoiceReconciliationResultUcpCapabilities:
    """
    Attributes:
        ai_pleaxy_procurement_reconciliation (Union[Unset,
            List['GetInvoiceReconciliationResultUcpCapabilitiesAiPleaxyProcurementReconciliationItem']]):
    """

    ai_pleaxy_procurement_reconciliation: Union[
        Unset,
        List[
            "GetInvoiceReconciliationResultUcpCapabilitiesAiPleaxyProcurementReconciliationItem"
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ai_pleaxy_procurement_reconciliation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ai_pleaxy_procurement_reconciliation, Unset):
            ai_pleaxy_procurement_reconciliation = []
            for (
                ai_pleaxy_procurement_reconciliation_item_data
            ) in self.ai_pleaxy_procurement_reconciliation:
                ai_pleaxy_procurement_reconciliation_item = (
                    ai_pleaxy_procurement_reconciliation_item_data.to_dict()
                )
                ai_pleaxy_procurement_reconciliation.append(
                    ai_pleaxy_procurement_reconciliation_item
                )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ai_pleaxy_procurement_reconciliation is not UNSET:
            field_dict["ai.pleaxy.procurement.reconciliation"] = (
                ai_pleaxy_procurement_reconciliation
            )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_invoice_reconciliation_result_ucp_capabilities_ai_pleaxy_procurement_reconciliation_item import (
            GetInvoiceReconciliationResultUcpCapabilitiesAiPleaxyProcurementReconciliationItem,
        )

        d = src_dict.copy()
        ai_pleaxy_procurement_reconciliation = []
        _ai_pleaxy_procurement_reconciliation = d.pop(
            "ai.pleaxy.procurement.reconciliation", UNSET
        )
        for ai_pleaxy_procurement_reconciliation_item_data in (
            _ai_pleaxy_procurement_reconciliation or []
        ):
            ai_pleaxy_procurement_reconciliation_item = GetInvoiceReconciliationResultUcpCapabilitiesAiPleaxyProcurementReconciliationItem.from_dict(
                ai_pleaxy_procurement_reconciliation_item_data
            )

            ai_pleaxy_procurement_reconciliation.append(
                ai_pleaxy_procurement_reconciliation_item
            )

        get_invoice_reconciliation_result_ucp_capabilities = cls(
            ai_pleaxy_procurement_reconciliation=ai_pleaxy_procurement_reconciliation,
        )

        get_invoice_reconciliation_result_ucp_capabilities.additional_properties = d
        return get_invoice_reconciliation_result_ucp_capabilities

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
