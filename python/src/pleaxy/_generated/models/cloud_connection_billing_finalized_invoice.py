from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_billing_finalized_invoice_source import (
    CloudConnectionBillingFinalizedInvoiceSource,
    check_cloud_connection_billing_finalized_invoice_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_connection_billing_finalized_invoice_adjustments_item import (
        CloudConnectionBillingFinalizedInvoiceAdjustmentsItem,
    )


T = TypeVar("T", bound="CloudConnectionBillingFinalizedInvoice")


@_attrs_define
class CloudConnectionBillingFinalizedInvoice:
    """
    Attributes:
        period_label (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        as_of (Union[Unset, str]):
        currency (Union[Unset, str]):
        source (Union[Unset, CloudConnectionBillingFinalizedInvoiceSource]):
        amount_payable (Union[Unset, float]):
        adjustments (Union[Unset, List['CloudConnectionBillingFinalizedInvoiceAdjustmentsItem']]):
    """

    period_label: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    as_of: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    source: Union[Unset, CloudConnectionBillingFinalizedInvoiceSource] = UNSET
    amount_payable: Union[Unset, float] = UNSET
    adjustments: Union[
        Unset, List["CloudConnectionBillingFinalizedInvoiceAdjustmentsItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period_label = self.period_label

        total_amount = self.total_amount

        as_of = self.as_of

        currency = self.currency

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        amount_payable = self.amount_payable

        adjustments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = []
            for adjustments_item_data in self.adjustments:
                adjustments_item = adjustments_item_data.to_dict()
                adjustments.append(adjustments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_label is not UNSET:
            field_dict["periodLabel"] = period_label
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if currency is not UNSET:
            field_dict["currency"] = currency
        if source is not UNSET:
            field_dict["source"] = source
        if amount_payable is not UNSET:
            field_dict["amountPayable"] = amount_payable
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cloud_connection_billing_finalized_invoice_adjustments_item import (
            CloudConnectionBillingFinalizedInvoiceAdjustmentsItem,
        )

        d = src_dict.copy()
        period_label = d.pop("periodLabel", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        as_of = d.pop("asOf", UNSET)

        currency = d.pop("currency", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CloudConnectionBillingFinalizedInvoiceSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_cloud_connection_billing_finalized_invoice_source(_source)

        amount_payable = d.pop("amountPayable", UNSET)

        adjustments = []
        _adjustments = d.pop("adjustments", UNSET)
        for adjustments_item_data in _adjustments or []:
            adjustments_item = (
                CloudConnectionBillingFinalizedInvoiceAdjustmentsItem.from_dict(
                    adjustments_item_data
                )
            )

            adjustments.append(adjustments_item)

        cloud_connection_billing_finalized_invoice = cls(
            period_label=period_label,
            total_amount=total_amount,
            as_of=as_of,
            currency=currency,
            source=source,
            amount_payable=amount_payable,
            adjustments=adjustments,
        )

        cloud_connection_billing_finalized_invoice.additional_properties = d
        return cloud_connection_billing_finalized_invoice

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
