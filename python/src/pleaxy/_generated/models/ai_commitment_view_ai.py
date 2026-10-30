from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_commitment_view_ai_invoicer import (
    AiCommitmentViewAiInvoicer,
    check_ai_commitment_view_ai_invoicer,
)
from ..models.ai_commitment_view_ai_vendor import (
    AiCommitmentViewAiVendor,
    check_ai_commitment_view_ai_vendor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiCommitmentViewAi")


@_attrs_define
class AiCommitmentViewAi:
    """
    Attributes:
        invoicer (Union[Unset, AiCommitmentViewAiInvoicer]):
        vendor (Union[Unset, AiCommitmentViewAiVendor]):
        model (Union[Unset, str]):
        meter (Union[Unset, str]):
    """

    invoicer: Union[Unset, AiCommitmentViewAiInvoicer] = UNSET
    vendor: Union[Unset, AiCommitmentViewAiVendor] = UNSET
    model: Union[Unset, str] = UNSET
    meter: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        vendor: Union[Unset, str] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        model = self.model

        meter = self.meter

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if meter is not UNSET:
            field_dict["meter"] = meter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiCommitmentViewAiInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_commitment_view_ai_invoicer(_invoicer)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, AiCommitmentViewAiVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = check_ai_commitment_view_ai_vendor(_vendor)

        model = d.pop("model", UNSET)

        meter = d.pop("meter", UNSET)

        ai_commitment_view_ai = cls(
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            meter=meter,
        )

        ai_commitment_view_ai.additional_properties = d
        return ai_commitment_view_ai

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
