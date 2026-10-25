from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_connection_billing_current_period_estimate import (
        CloudConnectionBillingCurrentPeriodEstimate,
    )
    from ..models.cloud_connection_billing_finalized_invoice import (
        CloudConnectionBillingFinalizedInvoice,
    )
    from ..models.cloud_connection_billing_previous_finalized_invoice import (
        CloudConnectionBillingPreviousFinalizedInvoice,
    )


T = TypeVar("T", bound="CloudConnectionBilling")


@_attrs_define
class CloudConnectionBilling:
    """
    Attributes:
        finalized_invoice (Union[Unset, CloudConnectionBillingFinalizedInvoice]):
        previous_finalized_invoice (Union[Unset, CloudConnectionBillingPreviousFinalizedInvoice]):
        current_period_estimate (Union[Unset, CloudConnectionBillingCurrentPeriodEstimate]):
    """

    finalized_invoice: Union[Unset, "CloudConnectionBillingFinalizedInvoice"] = UNSET
    previous_finalized_invoice: Union[
        Unset, "CloudConnectionBillingPreviousFinalizedInvoice"
    ] = UNSET
    current_period_estimate: Union[
        Unset, "CloudConnectionBillingCurrentPeriodEstimate"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finalized_invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.finalized_invoice, Unset):
            finalized_invoice = self.finalized_invoice.to_dict()

        previous_finalized_invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_finalized_invoice, Unset):
            previous_finalized_invoice = self.previous_finalized_invoice.to_dict()

        current_period_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_period_estimate, Unset):
            current_period_estimate = self.current_period_estimate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finalized_invoice is not UNSET:
            field_dict["finalizedInvoice"] = finalized_invoice
        if previous_finalized_invoice is not UNSET:
            field_dict["previousFinalizedInvoice"] = previous_finalized_invoice
        if current_period_estimate is not UNSET:
            field_dict["currentPeriodEstimate"] = current_period_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cloud_connection_billing_current_period_estimate import (
            CloudConnectionBillingCurrentPeriodEstimate,
        )
        from ..models.cloud_connection_billing_finalized_invoice import (
            CloudConnectionBillingFinalizedInvoice,
        )
        from ..models.cloud_connection_billing_previous_finalized_invoice import (
            CloudConnectionBillingPreviousFinalizedInvoice,
        )

        d = src_dict.copy()
        _finalized_invoice = d.pop("finalizedInvoice", UNSET)
        finalized_invoice: Union[Unset, CloudConnectionBillingFinalizedInvoice]
        if isinstance(_finalized_invoice, Unset):
            finalized_invoice = UNSET
        else:
            finalized_invoice = CloudConnectionBillingFinalizedInvoice.from_dict(
                _finalized_invoice
            )

        _previous_finalized_invoice = d.pop("previousFinalizedInvoice", UNSET)
        previous_finalized_invoice: Union[
            Unset, CloudConnectionBillingPreviousFinalizedInvoice
        ]
        if isinstance(_previous_finalized_invoice, Unset):
            previous_finalized_invoice = UNSET
        else:
            previous_finalized_invoice = (
                CloudConnectionBillingPreviousFinalizedInvoice.from_dict(
                    _previous_finalized_invoice
                )
            )

        _current_period_estimate = d.pop("currentPeriodEstimate", UNSET)
        current_period_estimate: Union[
            Unset, CloudConnectionBillingCurrentPeriodEstimate
        ]
        if isinstance(_current_period_estimate, Unset):
            current_period_estimate = UNSET
        else:
            current_period_estimate = (
                CloudConnectionBillingCurrentPeriodEstimate.from_dict(
                    _current_period_estimate
                )
            )

        cloud_connection_billing = cls(
            finalized_invoice=finalized_invoice,
            previous_finalized_invoice=previous_finalized_invoice,
            current_period_estimate=current_period_estimate,
        )

        cloud_connection_billing.additional_properties = d
        return cloud_connection_billing

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
