from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiCostCenterRowAlert")


@_attrs_define
class AiCostCenterRowAlert:
    """
    Attributes:
        threshold (Union[Unset, float]):
        sent_at (Union[Unset, str]):
    """

    threshold: Union[Unset, float] = UNSET
    sent_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        threshold = self.threshold

        sent_at = self.sent_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        threshold = d.pop("threshold", UNSET)

        sent_at = d.pop("sentAt", UNSET)

        ai_cost_center_row_alert = cls(
            threshold=threshold,
            sent_at=sent_at,
        )

        ai_cost_center_row_alert.additional_properties = d
        return ai_cost_center_row_alert

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
