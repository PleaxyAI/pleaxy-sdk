from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSpendCheckPurchaseOrderLine")


@_attrs_define
class AiSpendCheckPurchaseOrderLine:
    """
    Attributes:
        po_id (Union[Unset, str]):
        line_no (Union[Unset, float]):
        remaining (Union[Unset, float]):
        over_by (Union[Unset, float]):
    """

    po_id: Union[Unset, str] = UNSET
    line_no: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    over_by: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        po_id = self.po_id

        line_no = self.line_no

        remaining = self.remaining

        over_by = self.over_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if over_by is not UNSET:
            field_dict["overBy"] = over_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        po_id = d.pop("poId", UNSET)

        line_no = d.pop("lineNo", UNSET)

        remaining = d.pop("remaining", UNSET)

        over_by = d.pop("overBy", UNSET)

        ai_spend_check_purchase_order_line = cls(
            po_id=po_id,
            line_no=line_no,
            remaining=remaining,
            over_by=over_by,
        )

        ai_spend_check_purchase_order_line.additional_properties = d
        return ai_spend_check_purchase_order_line

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
