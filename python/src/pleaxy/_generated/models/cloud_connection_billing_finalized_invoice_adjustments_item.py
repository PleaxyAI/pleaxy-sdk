from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_billing_finalized_invoice_adjustments_item_document_type import (
    CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType,
    check_cloud_connection_billing_finalized_invoice_adjustments_item_document_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionBillingFinalizedInvoiceAdjustmentsItem")


@_attrs_define
class CloudConnectionBillingFinalizedInvoiceAdjustmentsItem:
    """
    Attributes:
        document_type (Union[Unset, CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
    """

    document_type: Union[
        Unset, CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType
    ] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type

        amount = self.amount

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _document_type = d.pop("documentType", UNSET)
        document_type: Union[
            Unset, CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType
        ]
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = check_cloud_connection_billing_finalized_invoice_adjustments_item_document_type(
                _document_type
            )

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        cloud_connection_billing_finalized_invoice_adjustments_item = cls(
            document_type=document_type,
            amount=amount,
            currency=currency,
        )

        cloud_connection_billing_finalized_invoice_adjustments_item.additional_properties = d
        return cloud_connection_billing_finalized_invoice_adjustments_item

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
