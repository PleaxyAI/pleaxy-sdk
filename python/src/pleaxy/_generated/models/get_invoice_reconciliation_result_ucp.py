from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_invoice_reconciliation_result_ucp_capabilities import (
        GetInvoiceReconciliationResultUcpCapabilities,
    )


T = TypeVar("T", bound="GetInvoiceReconciliationResultUcp")


@_attrs_define
class GetInvoiceReconciliationResultUcp:
    """
    Attributes:
        version (Union[Unset, str]):
        capabilities (Union[Unset, GetInvoiceReconciliationResultUcpCapabilities]):
    """

    version: Union[Unset, str] = UNSET
    capabilities: Union[Unset, "GetInvoiceReconciliationResultUcpCapabilities"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        capabilities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_invoice_reconciliation_result_ucp_capabilities import (
            GetInvoiceReconciliationResultUcpCapabilities,
        )

        d = src_dict.copy()
        version = d.pop("version", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, GetInvoiceReconciliationResultUcpCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = GetInvoiceReconciliationResultUcpCapabilities.from_dict(
                _capabilities
            )

        get_invoice_reconciliation_result_ucp = cls(
            version=version,
            capabilities=capabilities,
        )

        get_invoice_reconciliation_result_ucp.additional_properties = d
        return get_invoice_reconciliation_result_ucp

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
