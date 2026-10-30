from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_po_line_suggestions_invoicer import (
    AiPoLineSuggestionsInvoicer,
    check_ai_po_line_suggestions_invoicer,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_po_line_suggestion import AiPoLineSuggestion


T = TypeVar("T", bound="AiPoLineSuggestions")


@_attrs_define
class AiPoLineSuggestions:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiPoLineSuggestionsInvoicer]):
        period (Union[Unset, str]):
        provider (Union[Unset, str]):
        supplier_connection_id (Union[Unset, str]):
        lines (Union[Unset, List['AiPoLineSuggestion']]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiPoLineSuggestionsInvoicer] = UNSET
    period: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    lines: Union[Unset, List["AiPoLineSuggestion"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        period = self.period

        provider = self.provider

        supplier_connection_id = self.supplier_connection_id

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if period is not UNSET:
            field_dict["period"] = period
        if provider is not UNSET:
            field_dict["provider"] = provider
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_po_line_suggestion import AiPoLineSuggestion

        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiPoLineSuggestionsInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_po_line_suggestions_invoicer(_invoicer)

        period = d.pop("period", UNSET)

        provider = d.pop("provider", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = AiPoLineSuggestion.from_dict(lines_item_data)

            lines.append(lines_item)

        ai_po_line_suggestions = cls(
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            period=period,
            provider=provider,
            supplier_connection_id=supplier_connection_id,
            lines=lines,
        )

        ai_po_line_suggestions.additional_properties = d
        return ai_po_line_suggestions

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
