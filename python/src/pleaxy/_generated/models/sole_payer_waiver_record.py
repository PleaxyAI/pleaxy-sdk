from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_access_removal import InvoiceAccessRemoval


T = TypeVar("T", bound="SolePayerWaiverRecord")


@_attrs_define
class SolePayerWaiverRecord:
    """
    Attributes:
        access_removed (Union[Unset, List['InvoiceAccessRemoval']]):
        access_removed_total (Union[Unset, float]):
    """

    access_removed: Union[Unset, List["InvoiceAccessRemoval"]] = UNSET
    access_removed_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_removed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_removed, Unset):
            access_removed = []
            for access_removed_item_data in self.access_removed:
                access_removed_item = access_removed_item_data.to_dict()
                access_removed.append(access_removed_item)

        access_removed_total = self.access_removed_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_removed is not UNSET:
            field_dict["accessRemoved"] = access_removed
        if access_removed_total is not UNSET:
            field_dict["accessRemovedTotal"] = access_removed_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_access_removal import InvoiceAccessRemoval

        d = src_dict.copy()
        access_removed = []
        _access_removed = d.pop("accessRemoved", UNSET)
        for access_removed_item_data in _access_removed or []:
            access_removed_item = InvoiceAccessRemoval.from_dict(
                access_removed_item_data
            )

            access_removed.append(access_removed_item)

        access_removed_total = d.pop("accessRemovedTotal", UNSET)

        sole_payer_waiver_record = cls(
            access_removed=access_removed,
            access_removed_total=access_removed_total,
        )

        sole_payer_waiver_record.additional_properties = d
        return sole_payer_waiver_record

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
