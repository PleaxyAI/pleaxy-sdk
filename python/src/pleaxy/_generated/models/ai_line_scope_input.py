from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_line_scope_input_invoicer import (
    AiLineScopeInputInvoicer,
    check_ai_line_scope_input_invoicer,
)
from ..models.ai_line_scope_input_meter import (
    AiLineScopeInputMeter,
    check_ai_line_scope_input_meter,
)
from ..models.ai_line_scope_input_vendor import (
    AiLineScopeInputVendor,
    check_ai_line_scope_input_vendor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiLineScopeInput")


@_attrs_define
class AiLineScopeInput:
    """
    Attributes:
        invoicer (AiLineScopeInputInvoicer): Who bills the line: a cloud or an AI provider.
        vendor (AiLineScopeInputVendor): The model's maker.
        model (str): The model id as billed, e.g. claude-sonnet-4-5 (GET /ai-rate-cards lists them).
        meter (AiLineScopeInputMeter): The meter; prepaid_credit for a prepaid credit purchase drawn down by the cost
            report.
        region (Union[Unset, str]): The region, where the model is priced by region.
    """

    invoicer: AiLineScopeInputInvoicer
    vendor: AiLineScopeInputVendor
    model: str
    meter: AiLineScopeInputMeter
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: str = self.invoicer

        vendor: str = self.vendor

        model = self.model

        meter: str = self.meter

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoicer": invoicer,
                "vendor": vendor,
                "model": model,
                "meter": meter,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer = check_ai_line_scope_input_invoicer(d.pop("invoicer"))

        vendor = check_ai_line_scope_input_vendor(d.pop("vendor"))

        model = d.pop("model")

        meter = check_ai_line_scope_input_meter(d.pop("meter"))

        region = d.pop("region", UNSET)

        ai_line_scope_input = cls(
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            meter=meter,
            region=region,
        )

        ai_line_scope_input.additional_properties = d
        return ai_line_scope_input

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
