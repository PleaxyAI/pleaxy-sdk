from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_destination_setup import FocusDestinationSetup
    from ..models.focus_destination_view_destination_type_0 import (
        FocusDestinationViewDestinationType0,
    )


T = TypeVar("T", bound="FocusDestinationView")


@_attrs_define
class FocusDestinationView:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        destination (Union['FocusDestinationViewDestinationType0', None, Unset]):
        setup (Union[Unset, FocusDestinationSetup]):
    """

    enabled: Union[Unset, bool] = UNSET
    destination: Union["FocusDestinationViewDestinationType0", None, Unset] = UNSET
    setup: Union[Unset, "FocusDestinationSetup"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.focus_destination_view_destination_type_0 import (
            FocusDestinationViewDestinationType0,
        )

        enabled = self.enabled

        destination: Union[Dict[str, Any], None, Unset]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, FocusDestinationViewDestinationType0):
            destination = self.destination.to_dict()
        else:
            destination = self.destination

        setup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.setup, Unset):
            setup = self.setup.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if setup is not UNSET:
            field_dict["setup"] = setup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_destination_setup import FocusDestinationSetup
        from ..models.focus_destination_view_destination_type_0 import (
            FocusDestinationViewDestinationType0,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        def _parse_destination(
            data: object,
        ) -> Union["FocusDestinationViewDestinationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = FocusDestinationViewDestinationType0.from_dict(
                    data
                )

                return destination_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["FocusDestinationViewDestinationType0", None, Unset], data
            )

        destination = _parse_destination(d.pop("destination", UNSET))

        _setup = d.pop("setup", UNSET)
        setup: Union[Unset, FocusDestinationSetup]
        if isinstance(_setup, Unset):
            setup = UNSET
        else:
            setup = FocusDestinationSetup.from_dict(_setup)

        focus_destination_view = cls(
            enabled=enabled,
            destination=destination,
            setup=setup,
        )

        focus_destination_view.additional_properties = d
        return focus_destination_view

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
