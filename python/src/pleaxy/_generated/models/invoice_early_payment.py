from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_early_payment_source import (
    InvoiceEarlyPaymentSource,
    check_invoice_early_payment_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_early_payment_offered_by import InvoiceEarlyPaymentOfferedBy


T = TypeVar("T", bound="InvoiceEarlyPayment")


@_attrs_define
class InvoiceEarlyPayment:
    """
    Attributes:
        percent (Union[Unset, float]):
        deadline (Union[Unset, str]):
        source (Union[Unset, InvoiceEarlyPaymentSource]):
        contract_id (Union[Unset, str]):
        offered_by (Union[Unset, InvoiceEarlyPaymentOfferedBy]):
        offered_at (Union[Unset, str]):
        standing (Union[Unset, bool]):
    """

    percent: Union[Unset, float] = UNSET
    deadline: Union[Unset, str] = UNSET
    source: Union[Unset, InvoiceEarlyPaymentSource] = UNSET
    contract_id: Union[Unset, str] = UNSET
    offered_by: Union[Unset, "InvoiceEarlyPaymentOfferedBy"] = UNSET
    offered_at: Union[Unset, str] = UNSET
    standing: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent = self.percent

        deadline = self.deadline

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        contract_id = self.contract_id

        offered_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.offered_by, Unset):
            offered_by = self.offered_by.to_dict()

        offered_at = self.offered_at

        standing = self.standing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent is not UNSET:
            field_dict["percent"] = percent
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if source is not UNSET:
            field_dict["source"] = source
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if offered_by is not UNSET:
            field_dict["offeredBy"] = offered_by
        if offered_at is not UNSET:
            field_dict["offeredAt"] = offered_at
        if standing is not UNSET:
            field_dict["standing"] = standing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_early_payment_offered_by import (
            InvoiceEarlyPaymentOfferedBy,
        )

        d = src_dict.copy()
        percent = d.pop("percent", UNSET)

        deadline = d.pop("deadline", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, InvoiceEarlyPaymentSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_invoice_early_payment_source(_source)

        contract_id = d.pop("contractId", UNSET)

        _offered_by = d.pop("offeredBy", UNSET)
        offered_by: Union[Unset, InvoiceEarlyPaymentOfferedBy]
        if isinstance(_offered_by, Unset):
            offered_by = UNSET
        else:
            offered_by = InvoiceEarlyPaymentOfferedBy.from_dict(_offered_by)

        offered_at = d.pop("offeredAt", UNSET)

        standing = d.pop("standing", UNSET)

        invoice_early_payment = cls(
            percent=percent,
            deadline=deadline,
            source=source,
            contract_id=contract_id,
            offered_by=offered_by,
            offered_at=offered_at,
            standing=standing,
        )

        invoice_early_payment.additional_properties = d
        return invoice_early_payment

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
