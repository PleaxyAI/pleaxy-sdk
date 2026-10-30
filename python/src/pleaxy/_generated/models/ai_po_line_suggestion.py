from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_po_line_suggestion_price_source import (
    AiPoLineSuggestionPriceSource,
    check_ai_po_line_suggestion_price_source,
)
from ..models.ai_po_line_suggestion_unit import (
    AiPoLineSuggestionUnit,
    check_ai_po_line_suggestion_unit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_po_line_suggestion_ai import AiPoLineSuggestionAi


T = TypeVar("T", bound="AiPoLineSuggestion")


@_attrs_define
class AiPoLineSuggestion:
    """
    Attributes:
        ai (Union[Unset, AiPoLineSuggestionAi]):
        unit (Union[Unset, AiPoLineSuggestionUnit]):
        qty (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        currency (Union[Unset, str]):
        price_source (Union[Unset, AiPoLineSuggestionPriceSource]):
        contract_id (Union[Unset, str]):
        contract_term_id (Union[Unset, str]):
        period_quantity (Union[Unset, float]):
        period_amount (Union[Unset, float]):
    """

    ai: Union[Unset, "AiPoLineSuggestionAi"] = UNSET
    unit: Union[Unset, AiPoLineSuggestionUnit] = UNSET
    qty: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    price_source: Union[Unset, AiPoLineSuggestionPriceSource] = UNSET
    contract_id: Union[Unset, str] = UNSET
    contract_term_id: Union[Unset, str] = UNSET
    period_quantity: Union[Unset, float] = UNSET
    period_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

        qty = self.qty

        unit_price = self.unit_price

        currency = self.currency

        price_source: Union[Unset, str] = UNSET
        if not isinstance(self.price_source, Unset):
            price_source = self.price_source

        contract_id = self.contract_id

        contract_term_id = self.contract_term_id

        period_quantity = self.period_quantity

        period_amount = self.period_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ai is not UNSET:
            field_dict["ai"] = ai
        if unit is not UNSET:
            field_dict["unit"] = unit
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if price_source is not UNSET:
            field_dict["priceSource"] = price_source
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_term_id is not UNSET:
            field_dict["contractTermId"] = contract_term_id
        if period_quantity is not UNSET:
            field_dict["periodQuantity"] = period_quantity
        if period_amount is not UNSET:
            field_dict["periodAmount"] = period_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_po_line_suggestion_ai import AiPoLineSuggestionAi

        d = src_dict.copy()
        _ai = d.pop("ai", UNSET)
        ai: Union[Unset, AiPoLineSuggestionAi]
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = AiPoLineSuggestionAi.from_dict(_ai)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, AiPoLineSuggestionUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_ai_po_line_suggestion_unit(_unit)

        qty = d.pop("qty", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        _price_source = d.pop("priceSource", UNSET)
        price_source: Union[Unset, AiPoLineSuggestionPriceSource]
        if isinstance(_price_source, Unset):
            price_source = UNSET
        else:
            price_source = check_ai_po_line_suggestion_price_source(_price_source)

        contract_id = d.pop("contractId", UNSET)

        contract_term_id = d.pop("contractTermId", UNSET)

        period_quantity = d.pop("periodQuantity", UNSET)

        period_amount = d.pop("periodAmount", UNSET)

        ai_po_line_suggestion = cls(
            ai=ai,
            unit=unit,
            qty=qty,
            unit_price=unit_price,
            currency=currency,
            price_source=price_source,
            contract_id=contract_id,
            contract_term_id=contract_term_id,
            period_quantity=period_quantity,
            period_amount=period_amount,
        )

        ai_po_line_suggestion.additional_properties = d
        return ai_po_line_suggestion

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
