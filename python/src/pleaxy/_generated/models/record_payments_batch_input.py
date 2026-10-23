from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record_payment_item_input import RecordPaymentItemInput


T = TypeVar("T", bound="RecordPaymentsBatchInput")


@_attrs_define
class RecordPaymentsBatchInput:
    """
    Attributes:
        payments (List['RecordPaymentItemInput']):
    """

    payments: List["RecordPaymentItemInput"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_payment_item_input import RecordPaymentItemInput

        d = src_dict.copy()
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = RecordPaymentItemInput.from_dict(payments_item_data)

            payments.append(payments_item)

        record_payments_batch_input = cls(
            payments=payments,
        )

        record_payments_batch_input.additional_properties = d
        return record_payments_batch_input

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
