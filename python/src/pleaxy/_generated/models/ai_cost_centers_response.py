from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_cost_center_row import AiCostCenterRow
    from ..models.ai_cost_centers_response_unattributed_item import (
        AiCostCentersResponseUnattributedItem,
    )


T = TypeVar("T", bound="AiCostCentersResponse")


@_attrs_define
class AiCostCentersResponse:
    """
    Attributes:
        period (Union[Unset, str]):
        budget_mode (Union[Unset, str]):
        rows (Union[Unset, List['AiCostCenterRow']]):
        unattributed (Union[Unset, List['AiCostCentersResponseUnattributedItem']]):
        thresholds (Union[Unset, List[float]]):
    """

    period: Union[Unset, str] = UNSET
    budget_mode: Union[Unset, str] = UNSET
    rows: Union[Unset, List["AiCostCenterRow"]] = UNSET
    unattributed: Union[Unset, List["AiCostCentersResponseUnattributedItem"]] = UNSET
    thresholds: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        budget_mode = self.budget_mode

        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        unattributed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unattributed, Unset):
            unattributed = []
            for unattributed_item_data in self.unattributed:
                unattributed_item = unattributed_item_data.to_dict()
                unattributed.append(unattributed_item)

        thresholds: Union[Unset, List[float]] = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = self.thresholds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if budget_mode is not UNSET:
            field_dict["budgetMode"] = budget_mode
        if rows is not UNSET:
            field_dict["rows"] = rows
        if unattributed is not UNSET:
            field_dict["unattributed"] = unattributed
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_cost_center_row import AiCostCenterRow
        from ..models.ai_cost_centers_response_unattributed_item import (
            AiCostCentersResponseUnattributedItem,
        )

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        budget_mode = d.pop("budgetMode", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = AiCostCenterRow.from_dict(rows_item_data)

            rows.append(rows_item)

        unattributed = []
        _unattributed = d.pop("unattributed", UNSET)
        for unattributed_item_data in _unattributed or []:
            unattributed_item = AiCostCentersResponseUnattributedItem.from_dict(
                unattributed_item_data
            )

            unattributed.append(unattributed_item)

        thresholds = cast(List[float], d.pop("thresholds", UNSET))

        ai_cost_centers_response = cls(
            period=period,
            budget_mode=budget_mode,
            rows=rows,
            unattributed=unattributed,
            thresholds=thresholds,
        )

        ai_cost_centers_response.additional_properties = d
        return ai_cost_centers_response

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
