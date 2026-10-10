from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remittance_check_changed_fields_item import (
    RemittanceCheckChangedFieldsItem,
    check_remittance_check_changed_fields_item,
)
from ..models.remittance_check_status import (
    RemittanceCheckStatus,
    check_remittance_check_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemittanceCheck")


@_attrs_define
class RemittanceCheck:
    """
    Attributes:
        status (Union[Unset, RemittanceCheckStatus]):
        compared_invoice_id (Union[Unset, str]):
        compared_invoice_number (Union[Unset, str]):
        changed_fields (Union[Unset, List[RemittanceCheckChangedFieldsItem]]):
    """

    status: Union[Unset, RemittanceCheckStatus] = UNSET
    compared_invoice_id: Union[Unset, str] = UNSET
    compared_invoice_number: Union[Unset, str] = UNSET
    changed_fields: Union[Unset, List[RemittanceCheckChangedFieldsItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        compared_invoice_id = self.compared_invoice_id

        compared_invoice_number = self.compared_invoice_number

        changed_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.changed_fields, Unset):
            changed_fields = []
            for changed_fields_item_data in self.changed_fields:
                changed_fields_item: str = changed_fields_item_data
                changed_fields.append(changed_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if compared_invoice_id is not UNSET:
            field_dict["comparedInvoiceId"] = compared_invoice_id
        if compared_invoice_number is not UNSET:
            field_dict["comparedInvoiceNumber"] = compared_invoice_number
        if changed_fields is not UNSET:
            field_dict["changedFields"] = changed_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, RemittanceCheckStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_remittance_check_status(_status)

        compared_invoice_id = d.pop("comparedInvoiceId", UNSET)

        compared_invoice_number = d.pop("comparedInvoiceNumber", UNSET)

        changed_fields = []
        _changed_fields = d.pop("changedFields", UNSET)
        for changed_fields_item_data in _changed_fields or []:
            changed_fields_item = check_remittance_check_changed_fields_item(
                changed_fields_item_data
            )

            changed_fields.append(changed_fields_item)

        remittance_check = cls(
            status=status,
            compared_invoice_id=compared_invoice_id,
            compared_invoice_number=compared_invoice_number,
            changed_fields=changed_fields,
        )

        remittance_check.additional_properties = d
        return remittance_check

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
