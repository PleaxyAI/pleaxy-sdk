from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_ref import ImageRef


T = TypeVar("T", bound="ProfileImages")


@_attrs_define
class ProfileImages:
    """
    Attributes:
        profile (Union[Unset, ImageRef]):
        company (Union[Unset, ImageRef]):
    """

    profile: Union[Unset, "ImageRef"] = UNSET
    company: Union[Unset, "ImageRef"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        company: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_ref import ImageRef

        d = src_dict.copy()
        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, ImageRef]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = ImageRef.from_dict(_profile)

        _company = d.pop("company", UNSET)
        company: Union[Unset, ImageRef]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = ImageRef.from_dict(_company)

        profile_images = cls(
            profile=profile,
            company=company,
        )

        profile_images.additional_properties = d
        return profile_images

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
