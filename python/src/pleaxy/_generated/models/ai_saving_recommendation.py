from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_saving_recommendation_invoicer import (
    AiSavingRecommendationInvoicer,
    check_ai_saving_recommendation_invoicer,
)
from ..models.ai_saving_recommendation_kind import (
    AiSavingRecommendationKind,
    check_ai_saving_recommendation_kind,
)
from ..models.ai_saving_recommendation_vendor import (
    AiSavingRecommendationVendor,
    check_ai_saving_recommendation_vendor,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_saving_recommendation_detail import AiSavingRecommendationDetail


T = TypeVar("T", bound="AiSavingRecommendation")


@_attrs_define
class AiSavingRecommendation:
    """
    Attributes:
        kind (Union[Unset, AiSavingRecommendationKind]):
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiSavingRecommendationInvoicer]):
        label (Union[Unset, str]):
        vendor (Union[Unset, AiSavingRecommendationVendor]):
        model (Union[Unset, str]):
        currency (Union[Unset, str]):
        spend (Union[Unset, float]):
        saving (Union[Unset, float]):
        detail (Union[Unset, AiSavingRecommendationDetail]):
    """

    kind: Union[Unset, AiSavingRecommendationKind] = UNSET
    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiSavingRecommendationInvoicer] = UNSET
    label: Union[Unset, str] = UNSET
    vendor: Union[Unset, AiSavingRecommendationVendor] = UNSET
    model: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    spend: Union[Unset, float] = UNSET
    saving: Union[Unset, float] = UNSET
    detail: Union[Unset, "AiSavingRecommendationDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        label = self.label

        vendor: Union[Unset, str] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        model = self.model

        currency = self.currency

        spend = self.spend

        saving = self.saving

        detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if label is not UNSET:
            field_dict["label"] = label
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if currency is not UNSET:
            field_dict["currency"] = currency
        if spend is not UNSET:
            field_dict["spend"] = spend
        if saving is not UNSET:
            field_dict["saving"] = saving
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_saving_recommendation_detail import (
            AiSavingRecommendationDetail,
        )

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, AiSavingRecommendationKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_ai_saving_recommendation_kind(_kind)

        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiSavingRecommendationInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_saving_recommendation_invoicer(_invoicer)

        label = d.pop("label", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, AiSavingRecommendationVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = check_ai_saving_recommendation_vendor(_vendor)

        model = d.pop("model", UNSET)

        currency = d.pop("currency", UNSET)

        spend = d.pop("spend", UNSET)

        saving = d.pop("saving", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: Union[Unset, AiSavingRecommendationDetail]
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = AiSavingRecommendationDetail.from_dict(_detail)

        ai_saving_recommendation = cls(
            kind=kind,
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            label=label,
            vendor=vendor,
            model=model,
            currency=currency,
            spend=spend,
            saving=saving,
            detail=detail,
        )

        ai_saving_recommendation.additional_properties = d
        return ai_saving_recommendation

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
