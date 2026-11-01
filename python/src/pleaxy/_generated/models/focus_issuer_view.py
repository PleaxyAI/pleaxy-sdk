from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_issuer_view_mapped_by import (
    FocusIssuerViewMappedBy,
    check_focus_issuer_view_mapped_by,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_issuer_view_totals import FocusIssuerViewTotals


T = TypeVar("T", bound="FocusIssuerView")


@_attrs_define
class FocusIssuerView:
    """
    Attributes:
        issuer (Union[Unset, str]):
        supplier_connection_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        mapped_by (Union[Unset, FocusIssuerViewMappedBy]):
        totals (Union[Unset, FocusIssuerViewTotals]):
    """

    issuer: Union[Unset, str] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    mapped_by: Union[Unset, FocusIssuerViewMappedBy] = UNSET
    totals: Union[Unset, "FocusIssuerViewTotals"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer = self.issuer

        supplier_connection_id = self.supplier_connection_id

        supplier_name = self.supplier_name

        mapped_by: Union[Unset, str] = UNSET
        if not isinstance(self.mapped_by, Unset):
            mapped_by = self.mapped_by

        totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if mapped_by is not UNSET:
            field_dict["mappedBy"] = mapped_by
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_issuer_view_totals import FocusIssuerViewTotals

        d = src_dict.copy()
        issuer = d.pop("issuer", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        _mapped_by = d.pop("mappedBy", UNSET)
        mapped_by: Union[Unset, FocusIssuerViewMappedBy]
        if isinstance(_mapped_by, Unset):
            mapped_by = UNSET
        else:
            mapped_by = check_focus_issuer_view_mapped_by(_mapped_by)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, FocusIssuerViewTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = FocusIssuerViewTotals.from_dict(_totals)

        focus_issuer_view = cls(
            issuer=issuer,
            supplier_connection_id=supplier_connection_id,
            supplier_name=supplier_name,
            mapped_by=mapped_by,
            totals=totals,
        )

        focus_issuer_view.additional_properties = d
        return focus_issuer_view

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
