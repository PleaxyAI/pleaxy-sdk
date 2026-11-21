from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.e_invoice_vat import EInvoiceVat


T = TypeVar("T", bound="InvoiceEInvoiceDetails")


@_attrs_define
class InvoiceEInvoiceDetails:
    """
    Attributes:
        line_vat (Union[Unset, List['EInvoiceVat']]):
        adjustment_vat (Union[Unset, List['EInvoiceVat']]):
        exemption_reason (Union[Unset, str]):
        exemption_reason_code (Union[Unset, str]):
        buyer_reference (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        updated_by (Union[Unset, str]):
    """

    line_vat: Union[Unset, List["EInvoiceVat"]] = UNSET
    adjustment_vat: Union[Unset, List["EInvoiceVat"]] = UNSET
    exemption_reason: Union[Unset, str] = UNSET
    exemption_reason_code: Union[Unset, str] = UNSET
    buyer_reference: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_vat: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_vat, Unset):
            line_vat = []
            for line_vat_item_data in self.line_vat:
                line_vat_item = line_vat_item_data.to_dict()
                line_vat.append(line_vat_item)

        adjustment_vat: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustment_vat, Unset):
            adjustment_vat = []
            for adjustment_vat_item_data in self.adjustment_vat:
                adjustment_vat_item = adjustment_vat_item_data.to_dict()
                adjustment_vat.append(adjustment_vat_item)

        exemption_reason = self.exemption_reason

        exemption_reason_code = self.exemption_reason_code

        buyer_reference = self.buyer_reference

        updated_at = self.updated_at

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_vat is not UNSET:
            field_dict["lineVat"] = line_vat
        if adjustment_vat is not UNSET:
            field_dict["adjustmentVat"] = adjustment_vat
        if exemption_reason is not UNSET:
            field_dict["exemptionReason"] = exemption_reason
        if exemption_reason_code is not UNSET:
            field_dict["exemptionReasonCode"] = exemption_reason_code
        if buyer_reference is not UNSET:
            field_dict["buyerReference"] = buyer_reference
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.e_invoice_vat import EInvoiceVat

        d = src_dict.copy()
        line_vat = []
        _line_vat = d.pop("lineVat", UNSET)
        for line_vat_item_data in _line_vat or []:
            line_vat_item = EInvoiceVat.from_dict(line_vat_item_data)

            line_vat.append(line_vat_item)

        adjustment_vat = []
        _adjustment_vat = d.pop("adjustmentVat", UNSET)
        for adjustment_vat_item_data in _adjustment_vat or []:
            adjustment_vat_item = EInvoiceVat.from_dict(adjustment_vat_item_data)

            adjustment_vat.append(adjustment_vat_item)

        exemption_reason = d.pop("exemptionReason", UNSET)

        exemption_reason_code = d.pop("exemptionReasonCode", UNSET)

        buyer_reference = d.pop("buyerReference", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        invoice_e_invoice_details = cls(
            line_vat=line_vat,
            adjustment_vat=adjustment_vat,
            exemption_reason=exemption_reason,
            exemption_reason_code=exemption_reason_code,
            buyer_reference=buyer_reference,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        invoice_e_invoice_details.additional_properties = d
        return invoice_e_invoice_details

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
