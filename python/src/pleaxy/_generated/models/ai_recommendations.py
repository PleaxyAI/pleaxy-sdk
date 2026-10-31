from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_saving_recommendation import AiSavingRecommendation
    from ..models.ai_uncovered_spend import AiUncoveredSpend


T = TypeVar("T", bound="AiRecommendations")


@_attrs_define
class AiRecommendations:
    """
    Attributes:
        period (Union[Unset, str]):
        basis_period (Union[Unset, str]):
        uncovered (Union[Unset, List['AiUncoveredSpend']]):
        accounts (Union[Unset, List['AiUncoveredSpend']]):
        savings (Union[Unset, List['AiSavingRecommendation']]):
    """

    period: Union[Unset, str] = UNSET
    basis_period: Union[Unset, str] = UNSET
    uncovered: Union[Unset, List["AiUncoveredSpend"]] = UNSET
    accounts: Union[Unset, List["AiUncoveredSpend"]] = UNSET
    savings: Union[Unset, List["AiSavingRecommendation"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        basis_period = self.basis_period

        uncovered: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.uncovered, Unset):
            uncovered = []
            for uncovered_item_data in self.uncovered:
                uncovered_item = uncovered_item_data.to_dict()
                uncovered.append(uncovered_item)

        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        savings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.savings, Unset):
            savings = []
            for savings_item_data in self.savings:
                savings_item = savings_item_data.to_dict()
                savings.append(savings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if basis_period is not UNSET:
            field_dict["basisPeriod"] = basis_period
        if uncovered is not UNSET:
            field_dict["uncovered"] = uncovered
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if savings is not UNSET:
            field_dict["savings"] = savings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_saving_recommendation import AiSavingRecommendation
        from ..models.ai_uncovered_spend import AiUncoveredSpend

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        basis_period = d.pop("basisPeriod", UNSET)

        uncovered = []
        _uncovered = d.pop("uncovered", UNSET)
        for uncovered_item_data in _uncovered or []:
            uncovered_item = AiUncoveredSpend.from_dict(uncovered_item_data)

            uncovered.append(uncovered_item)

        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = AiUncoveredSpend.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        savings = []
        _savings = d.pop("savings", UNSET)
        for savings_item_data in _savings or []:
            savings_item = AiSavingRecommendation.from_dict(savings_item_data)

            savings.append(savings_item)

        ai_recommendations = cls(
            period=period,
            basis_period=basis_period,
            uncovered=uncovered,
            accounts=accounts,
            savings=savings,
        )

        ai_recommendations.additional_properties = d
        return ai_recommendations

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
