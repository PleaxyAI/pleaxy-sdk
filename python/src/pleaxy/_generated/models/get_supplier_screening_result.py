from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_screening import SupplierScreening


T = TypeVar("T", bound="GetSupplierScreeningResult")


@_attrs_define
class GetSupplierScreeningResult:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        screening (Union[Unset, SupplierScreening]):
    """

    enabled: Union[Unset, bool] = UNSET
    screening: Union[Unset, "SupplierScreening"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        screening: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.screening, Unset):
            screening = self.screening.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if screening is not UNSET:
            field_dict["screening"] = screening

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_screening import SupplierScreening

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _screening = d.pop("screening", UNSET)
        screening: Union[Unset, SupplierScreening]
        if isinstance(_screening, Unset):
            screening = UNSET
        else:
            screening = SupplierScreening.from_dict(_screening)

        get_supplier_screening_result = cls(
            enabled=enabled,
            screening=screening,
        )

        get_supplier_screening_result.additional_properties = d
        return get_supplier_screening_result

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
