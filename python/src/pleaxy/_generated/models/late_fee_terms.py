from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.late_fee_terms_basis import LateFeeTermsBasis, check_late_fee_terms_basis
from ..models.late_fee_terms_statute import (
    LateFeeTermsStatute,
    check_late_fee_terms_statute,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.late_fee_terms_interest import LateFeeTermsInterest


T = TypeVar("T", bound="LateFeeTerms")


@_attrs_define
class LateFeeTerms:
    """
    Attributes:
        grace_days (Union[Unset, float]):
        basis (Union[Unset, LateFeeTermsBasis]):
        statute (Union[Unset, LateFeeTermsStatute]):
        statute_country (Union[Unset, str]):
        interest (Union[Unset, LateFeeTermsInterest]):
        fixed_charge (Union[Unset, float]):
    """

    grace_days: Union[Unset, float] = UNSET
    basis: Union[Unset, LateFeeTermsBasis] = UNSET
    statute: Union[Unset, LateFeeTermsStatute] = UNSET
    statute_country: Union[Unset, str] = UNSET
    interest: Union[Unset, "LateFeeTermsInterest"] = UNSET
    fixed_charge: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grace_days = self.grace_days

        basis: Union[Unset, str] = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis

        statute: Union[Unset, str] = UNSET
        if not isinstance(self.statute, Unset):
            statute = self.statute

        statute_country = self.statute_country

        interest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.to_dict()

        fixed_charge = self.fixed_charge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grace_days is not UNSET:
            field_dict["graceDays"] = grace_days
        if basis is not UNSET:
            field_dict["basis"] = basis
        if statute is not UNSET:
            field_dict["statute"] = statute
        if statute_country is not UNSET:
            field_dict["statuteCountry"] = statute_country
        if interest is not UNSET:
            field_dict["interest"] = interest
        if fixed_charge is not UNSET:
            field_dict["fixedCharge"] = fixed_charge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.late_fee_terms_interest import LateFeeTermsInterest

        d = src_dict.copy()
        grace_days = d.pop("graceDays", UNSET)

        _basis = d.pop("basis", UNSET)
        basis: Union[Unset, LateFeeTermsBasis]
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_late_fee_terms_basis(_basis)

        _statute = d.pop("statute", UNSET)
        statute: Union[Unset, LateFeeTermsStatute]
        if isinstance(_statute, Unset):
            statute = UNSET
        else:
            statute = check_late_fee_terms_statute(_statute)

        statute_country = d.pop("statuteCountry", UNSET)

        _interest = d.pop("interest", UNSET)
        interest: Union[Unset, LateFeeTermsInterest]
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = LateFeeTermsInterest.from_dict(_interest)

        fixed_charge = d.pop("fixedCharge", UNSET)

        late_fee_terms = cls(
            grace_days=grace_days,
            basis=basis,
            statute=statute,
            statute_country=statute_country,
            interest=interest,
            fixed_charge=fixed_charge,
        )

        late_fee_terms.additional_properties = d
        return late_fee_terms

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
