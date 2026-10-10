from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_counterparty import InvoiceCounterparty


T = TypeVar("T", bound="ListInvoiceCounterpartiesResult")


@_attrs_define
class ListInvoiceCounterpartiesResult:
    """
    Attributes:
        counterparties (Union[Unset, List['InvoiceCounterparty']]):
    """

    counterparties: Union[Unset, List["InvoiceCounterparty"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counterparties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.counterparties, Unset):
            counterparties = []
            for counterparties_item_data in self.counterparties:
                counterparties_item = counterparties_item_data.to_dict()
                counterparties.append(counterparties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counterparties is not UNSET:
            field_dict["counterparties"] = counterparties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_counterparty import InvoiceCounterparty

        d = src_dict.copy()
        counterparties = []
        _counterparties = d.pop("counterparties", UNSET)
        for counterparties_item_data in _counterparties or []:
            counterparties_item = InvoiceCounterparty.from_dict(
                counterparties_item_data
            )

            counterparties.append(counterparties_item)

        list_invoice_counterparties_result = cls(
            counterparties=counterparties,
        )

        list_invoice_counterparties_result.additional_properties = d
        return list_invoice_counterparties_result

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
