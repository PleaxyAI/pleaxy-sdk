from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tier_finding_excess import TierFindingExcess, check_tier_finding_excess
from ..models.tier_finding_type import TierFindingType, check_tier_finding_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="TierFinding")


@_attrs_define
class TierFinding:
    """
    Attributes:
        type (Union[Unset, TierFindingType]):
        billed (Union[Unset, float]):
        projected (Union[Unset, float]):
        total (Union[Unset, float]):
        tier_from (Union[Unset, float]):
        percent (Union[Unset, float]):
        window_start (Union[Unset, str]):
        window_end (Union[Unset, str]):
        excess (Union[Unset, TierFindingExcess]):
        contract_id (Union[Unset, str]):
        contract_title (Union[Unset, str]):
        supplier (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    type: Union[Unset, TierFindingType] = UNSET
    billed: Union[Unset, float] = UNSET
    projected: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    tier_from: Union[Unset, float] = UNSET
    percent: Union[Unset, float] = UNSET
    window_start: Union[Unset, str] = UNSET
    window_end: Union[Unset, str] = UNSET
    excess: Union[Unset, TierFindingExcess] = UNSET
    contract_id: Union[Unset, str] = UNSET
    contract_title: Union[Unset, str] = UNSET
    supplier: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        billed = self.billed

        projected = self.projected

        total = self.total

        tier_from = self.tier_from

        percent = self.percent

        window_start = self.window_start

        window_end = self.window_end

        excess: Union[Unset, int] = UNSET
        if not isinstance(self.excess, Unset):
            excess = self.excess

        contract_id = self.contract_id

        contract_title = self.contract_title

        supplier = self.supplier

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if billed is not UNSET:
            field_dict["billed"] = billed
        if projected is not UNSET:
            field_dict["projected"] = projected
        if total is not UNSET:
            field_dict["total"] = total
        if tier_from is not UNSET:
            field_dict["tierFrom"] = tier_from
        if percent is not UNSET:
            field_dict["percent"] = percent
        if window_start is not UNSET:
            field_dict["windowStart"] = window_start
        if window_end is not UNSET:
            field_dict["windowEnd"] = window_end
        if excess is not UNSET:
            field_dict["excess"] = excess
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_title is not UNSET:
            field_dict["contractTitle"] = contract_title
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TierFindingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_tier_finding_type(_type)

        billed = d.pop("billed", UNSET)

        projected = d.pop("projected", UNSET)

        total = d.pop("total", UNSET)

        tier_from = d.pop("tierFrom", UNSET)

        percent = d.pop("percent", UNSET)

        window_start = d.pop("windowStart", UNSET)

        window_end = d.pop("windowEnd", UNSET)

        _excess = d.pop("excess", UNSET)
        excess: Union[Unset, TierFindingExcess]
        if isinstance(_excess, Unset):
            excess = UNSET
        else:
            excess = check_tier_finding_excess(_excess)

        contract_id = d.pop("contractId", UNSET)

        contract_title = d.pop("contractTitle", UNSET)

        supplier = d.pop("supplier", UNSET)

        currency = d.pop("currency", UNSET)

        tier_finding = cls(
            type=type,
            billed=billed,
            projected=projected,
            total=total,
            tier_from=tier_from,
            percent=percent,
            window_start=window_start,
            window_end=window_end,
            excess=excess,
            contract_id=contract_id,
            contract_title=contract_title,
            supplier=supplier,
            currency=currency,
        )

        tier_finding.additional_properties = d
        return tier_finding

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
