from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credit_application_input import CreditApplicationInput


T = TypeVar("T", bound="ApplyCreditsInput")


@_attrs_define
class ApplyCreditsInput:
    """
    Attributes:
        applications (List['CreditApplicationInput']): All or none, in one write. 1–20.
    """

    applications: List["CreditApplicationInput"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        applications = []
        for applications_item_data in self.applications:
            applications_item = applications_item_data.to_dict()
            applications.append(applications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applications": applications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_application_input import CreditApplicationInput

        d = src_dict.copy()
        applications = []
        _applications = d.pop("applications")
        for applications_item_data in _applications:
            applications_item = CreditApplicationInput.from_dict(applications_item_data)

            applications.append(applications_item)

        apply_credits_input = cls(
            applications=applications,
        )

        apply_credits_input.additional_properties = d
        return apply_credits_input

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
