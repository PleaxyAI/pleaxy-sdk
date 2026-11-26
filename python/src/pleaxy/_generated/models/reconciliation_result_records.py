from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconciliation_result_records_order import (
        ReconciliationResultRecordsOrder,
    )
    from ..models.reconciliation_result_records_price_agreement import (
        ReconciliationResultRecordsPriceAgreement,
    )
    from ..models.reconciliation_result_records_usage import (
        ReconciliationResultRecordsUsage,
    )


T = TypeVar("T", bound="ReconciliationResultRecords")


@_attrs_define
class ReconciliationResultRecords:
    """
    Attributes:
        order (Union[Unset, ReconciliationResultRecordsOrder]):
        price_agreement (Union[Unset, ReconciliationResultRecordsPriceAgreement]):
        usage (Union[Unset, ReconciliationResultRecordsUsage]):
    """

    order: Union[Unset, "ReconciliationResultRecordsOrder"] = UNSET
    price_agreement: Union[Unset, "ReconciliationResultRecordsPriceAgreement"] = UNSET
    usage: Union[Unset, "ReconciliationResultRecordsUsage"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        price_agreement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price_agreement, Unset):
            price_agreement = self.price_agreement.to_dict()

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if price_agreement is not UNSET:
            field_dict["price_agreement"] = price_agreement
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reconciliation_result_records_order import (
            ReconciliationResultRecordsOrder,
        )
        from ..models.reconciliation_result_records_price_agreement import (
            ReconciliationResultRecordsPriceAgreement,
        )
        from ..models.reconciliation_result_records_usage import (
            ReconciliationResultRecordsUsage,
        )

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, ReconciliationResultRecordsOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = ReconciliationResultRecordsOrder.from_dict(_order)

        _price_agreement = d.pop("price_agreement", UNSET)
        price_agreement: Union[Unset, ReconciliationResultRecordsPriceAgreement]
        if isinstance(_price_agreement, Unset):
            price_agreement = UNSET
        else:
            price_agreement = ReconciliationResultRecordsPriceAgreement.from_dict(
                _price_agreement
            )

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ReconciliationResultRecordsUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ReconciliationResultRecordsUsage.from_dict(_usage)

        reconciliation_result_records = cls(
            order=order,
            price_agreement=price_agreement,
            usage=usage,
        )

        reconciliation_result_records.additional_properties = d
        return reconciliation_result_records

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
