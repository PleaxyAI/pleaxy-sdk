from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoPoComparison")


@_attrs_define
class NoPoComparison:
    """
    Attributes:
        average (Union[Unset, float]):
        invoice_ids (Union[Unset, List[str]]):
        difference_pct (Union[Unset, float]):
        tolerance_pct (Union[Unset, float]):
        at (Union[Unset, str]):
    """

    average: Union[Unset, float] = UNSET
    invoice_ids: Union[Unset, List[str]] = UNSET
    difference_pct: Union[Unset, float] = UNSET
    tolerance_pct: Union[Unset, float] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average = self.average

        invoice_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.invoice_ids, Unset):
            invoice_ids = self.invoice_ids

        difference_pct = self.difference_pct

        tolerance_pct = self.tolerance_pct

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if invoice_ids is not UNSET:
            field_dict["invoiceIds"] = invoice_ids
        if difference_pct is not UNSET:
            field_dict["differencePct"] = difference_pct
        if tolerance_pct is not UNSET:
            field_dict["tolerancePct"] = tolerance_pct
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average = d.pop("average", UNSET)

        invoice_ids = cast(List[str], d.pop("invoiceIds", UNSET))

        difference_pct = d.pop("differencePct", UNSET)

        tolerance_pct = d.pop("tolerancePct", UNSET)

        at = d.pop("at", UNSET)

        no_po_comparison = cls(
            average=average,
            invoice_ids=invoice_ids,
            difference_pct=difference_pct,
            tolerance_pct=tolerance_pct,
            at=at,
        )

        no_po_comparison.additional_properties = d
        return no_po_comparison

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
