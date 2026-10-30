from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_seat_count_invoicer import (
    AiSeatCountInvoicer,
    check_ai_seat_count_invoicer,
)
from ..models.ai_seat_count_source import AiSeatCountSource, check_ai_seat_count_source
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSeatCount")


@_attrs_define
class AiSeatCount:
    """
    Attributes:
        invoicer (Union[Unset, AiSeatCountInvoicer]):
        product (Union[Unset, str]):
        period (Union[Unset, str]):
        active_users (Union[Unset, float]):
        source (Union[Unset, AiSeatCountSource]):
        recorded_at (Union[Unset, str]):
        recorded_by (Union[Unset, str]):
    """

    invoicer: Union[Unset, AiSeatCountInvoicer] = UNSET
    product: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    active_users: Union[Unset, float] = UNSET
    source: Union[Unset, AiSeatCountSource] = UNSET
    recorded_at: Union[Unset, str] = UNSET
    recorded_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        product = self.product

        period = self.period

        active_users = self.active_users

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        recorded_at = self.recorded_at

        recorded_by = self.recorded_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if product is not UNSET:
            field_dict["product"] = product
        if period is not UNSET:
            field_dict["period"] = period
        if active_users is not UNSET:
            field_dict["activeUsers"] = active_users
        if source is not UNSET:
            field_dict["source"] = source
        if recorded_at is not UNSET:
            field_dict["recordedAt"] = recorded_at
        if recorded_by is not UNSET:
            field_dict["recordedBy"] = recorded_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiSeatCountInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_seat_count_invoicer(_invoicer)

        product = d.pop("product", UNSET)

        period = d.pop("period", UNSET)

        active_users = d.pop("activeUsers", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, AiSeatCountSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_ai_seat_count_source(_source)

        recorded_at = d.pop("recordedAt", UNSET)

        recorded_by = d.pop("recordedBy", UNSET)

        ai_seat_count = cls(
            invoicer=invoicer,
            product=product,
            period=period,
            active_users=active_users,
            source=source,
            recorded_at=recorded_at,
            recorded_by=recorded_by,
        )

        ai_seat_count.additional_properties = d
        return ai_seat_count

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
