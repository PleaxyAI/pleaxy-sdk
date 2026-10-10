from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetWarningPctInput")


@_attrs_define
class SetWarningPctInput:
    """
    Attributes:
        warning_pct (float): Percent, 0–100: how far an invoice's stated rate may be from the reference before it's
            flagged.
    """

    warning_pct: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warning_pct = self.warning_pct

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warningPct": warning_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        warning_pct = d.pop("warningPct")

        set_warning_pct_input = cls(
            warning_pct=warning_pct,
        )

        set_warning_pct_input.additional_properties = d
        return set_warning_pct_input

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
