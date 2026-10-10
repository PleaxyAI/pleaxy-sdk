from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_rate import ReferenceRate


T = TypeVar("T", bound="GetReferenceRateResult")


@_attrs_define
class GetReferenceRateResult:
    """
    Attributes:
        reference (Union[Unset, ReferenceRate]):
    """

    reference: Union[Unset, "ReferenceRate"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference_rate import ReferenceRate

        d = src_dict.copy()
        _reference = d.pop("reference", UNSET)
        reference: Union[Unset, ReferenceRate]
        if isinstance(_reference, Unset):
            reference = UNSET
        else:
            reference = ReferenceRate.from_dict(_reference)

        get_reference_rate_result = cls(
            reference=reference,
        )

        get_reference_rate_result.additional_properties = d
        return get_reference_rate_result

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
