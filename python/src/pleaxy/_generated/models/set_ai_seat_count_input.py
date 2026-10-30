from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_ai_seat_count_input_invoicer import (
    SetAiSeatCountInputInvoicer,
    check_set_ai_seat_count_input_invoicer,
)
from ..models.set_ai_seat_count_input_source import (
    SetAiSeatCountInputSource,
    check_set_ai_seat_count_input_source,
)

T = TypeVar("T", bound="SetAiSeatCountInput")


@_attrs_define
class SetAiSeatCountInput:
    """
    Attributes:
        invoicer (SetAiSeatCountInputInvoicer): Who bills the seats.
        product (str): The seat product, as the order line names it (its ai.model), e.g. chatgpt-enterprise.
        period (str): The month, YYYY-MM.
        active_users (float): Active users in the identity provider that month: those holding a seat who signed in.
        source (SetAiSeatCountInputSource):
    """

    invoicer: SetAiSeatCountInputInvoicer
    product: str
    period: str
    active_users: float
    source: SetAiSeatCountInputSource
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: str = self.invoicer

        product = self.product

        period = self.period

        active_users = self.active_users

        source: str = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoicer": invoicer,
                "product": product,
                "period": period,
                "activeUsers": active_users,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer = check_set_ai_seat_count_input_invoicer(d.pop("invoicer"))

        product = d.pop("product")

        period = d.pop("period")

        active_users = d.pop("activeUsers")

        source = check_set_ai_seat_count_input_source(d.pop("source"))

        set_ai_seat_count_input = cls(
            invoicer=invoicer,
            product=product,
            period=period,
            active_users=active_users,
            source=source,
        )

        set_ai_seat_count_input.additional_properties = d
        return set_ai_seat_count_input

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
