from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_ai_line_input_invoicer import (
    InvoiceAiLineInputInvoicer,
    check_invoice_ai_line_input_invoicer,
)
from ..models.invoice_ai_line_input_meter import (
    InvoiceAiLineInputMeter,
    check_invoice_ai_line_input_meter,
)
from ..models.invoice_ai_line_input_vendor import (
    InvoiceAiLineInputVendor,
    check_invoice_ai_line_input_vendor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceAiLineInput")


@_attrs_define
class InvoiceAiLineInput:
    """
    Attributes:
        invoicer (InvoiceAiLineInputInvoicer): Who bills the line: a cloud or an AI provider.
        vendor (InvoiceAiLineInputVendor): The model's maker.
        model (str): The model id as billed, e.g. claude-sonnet-4-5 (GET /ai-rate-cards lists them).
        meter (InvoiceAiLineInputMeter): The meter; prepaid_credit for a prepaid credit purchase drawn down by the cost
            report.
        region (Union[Unset, str]): The region, where the model is priced by region.
        period (Union[Unset, str]): The month of usage the line bills, YYYY-MM. Defaults to the month before the invoice
            date.
    """

    invoicer: InvoiceAiLineInputInvoicer
    vendor: InvoiceAiLineInputVendor
    model: str
    meter: InvoiceAiLineInputMeter
    region: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: str = self.invoicer

        vendor: str = self.vendor

        model = self.model

        meter: str = self.meter

        region = self.region

        period = self.period

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
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer = check_invoice_ai_line_input_invoicer(d.pop("invoicer"))

        vendor = check_invoice_ai_line_input_vendor(d.pop("vendor"))

        model = d.pop("model")

        meter = check_invoice_ai_line_input_meter(d.pop("meter"))

        region = d.pop("region", UNSET)

        period = d.pop("period", UNSET)

        invoice_ai_line_input = cls(
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            meter=meter,
            region=region,
            period=period,
        )

        invoice_ai_line_input.additional_properties = d
        return invoice_ai_line_input

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
