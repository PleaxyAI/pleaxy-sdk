from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_result_checked_item_group import (
    ReconciliationResultCheckedItemGroup,
    check_reconciliation_result_checked_item_group,
)
from ..models.reconciliation_result_checked_item_result import (
    ReconciliationResultCheckedItemResult,
    check_reconciliation_result_checked_item_result,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationResultCheckedItem")


@_attrs_define
class ReconciliationResultCheckedItem:
    """
    Attributes:
        group (Union[Unset, ReconciliationResultCheckedItemGroup]):
        result (Union[Unset, ReconciliationResultCheckedItemResult]):
    """

    group: Union[Unset, ReconciliationResultCheckedItemGroup] = UNSET
    result: Union[Unset, ReconciliationResultCheckedItemResult] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group: Union[Unset, str] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _group = d.pop("group", UNSET)
        group: Union[Unset, ReconciliationResultCheckedItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = check_reconciliation_result_checked_item_group(_group)

        _result = d.pop("result", UNSET)
        result: Union[Unset, ReconciliationResultCheckedItemResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = check_reconciliation_result_checked_item_result(_result)

        reconciliation_result_checked_item = cls(
            group=group,
            result=result,
        )

        reconciliation_result_checked_item.additional_properties = d
        return reconciliation_result_checked_item

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
