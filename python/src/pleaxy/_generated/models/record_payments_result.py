from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_payments_result_results_item import (
        RecordPaymentsResultResultsItem,
    )


T = TypeVar("T", bound="RecordPaymentsResult")


@_attrs_define
class RecordPaymentsResult:
    """
    Attributes:
        results (Union[Unset, List['RecordPaymentsResultResultsItem']]):
        recorded (Union[Unset, float]):
        already_recorded (Union[Unset, float]):
        refused (Union[Unset, float]):
    """

    results: Union[Unset, List["RecordPaymentsResultResultsItem"]] = UNSET
    recorded: Union[Unset, float] = UNSET
    already_recorded: Union[Unset, float] = UNSET
    refused: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        recorded = self.recorded

        already_recorded = self.already_recorded

        refused = self.refused

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if recorded is not UNSET:
            field_dict["recorded"] = recorded
        if already_recorded is not UNSET:
            field_dict["alreadyRecorded"] = already_recorded
        if refused is not UNSET:
            field_dict["refused"] = refused

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_payments_result_results_item import (
            RecordPaymentsResultResultsItem,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = RecordPaymentsResultResultsItem.from_dict(results_item_data)

            results.append(results_item)

        recorded = d.pop("recorded", UNSET)

        already_recorded = d.pop("alreadyRecorded", UNSET)

        refused = d.pop("refused", UNSET)

        record_payments_result = cls(
            results=results,
            recorded=recorded,
            already_recorded=already_recorded,
            refused=refused,
        )

        record_payments_result.additional_properties = d
        return record_payments_result

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
