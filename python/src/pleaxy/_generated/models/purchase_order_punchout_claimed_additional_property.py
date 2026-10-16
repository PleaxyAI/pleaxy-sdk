from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_order_punchout_claimed_additional_property_operation_allowed import (
    PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed,
    check_purchase_order_punchout_claimed_additional_property_operation_allowed,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_punchout_claimed_additional_property_exact import (
        PurchaseOrderPunchoutClaimedAdditionalPropertyExact,
    )


T = TypeVar("T", bound="PurchaseOrderPunchoutClaimedAdditionalProperty")


@_attrs_define
class PurchaseOrderPunchoutClaimedAdditionalProperty:
    """
    Attributes:
        claim_floor (Union[Unset, float]):
        claimed_at (Union[Unset, str]):
        operation_allowed (Union[Unset, PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed]):
        order_by (Union[Unset, str]):
        exact (Union[Unset, PurchaseOrderPunchoutClaimedAdditionalPropertyExact]):
    """

    claim_floor: Union[Unset, float] = UNSET
    claimed_at: Union[Unset, str] = UNSET
    operation_allowed: Union[
        Unset, PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed
    ] = UNSET
    order_by: Union[Unset, str] = UNSET
    exact: Union[Unset, "PurchaseOrderPunchoutClaimedAdditionalPropertyExact"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        claim_floor = self.claim_floor

        claimed_at = self.claimed_at

        operation_allowed: Union[Unset, str] = UNSET
        if not isinstance(self.operation_allowed, Unset):
            operation_allowed = self.operation_allowed

        order_by = self.order_by

        exact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exact, Unset):
            exact = self.exact.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim_floor is not UNSET:
            field_dict["claimFloor"] = claim_floor
        if claimed_at is not UNSET:
            field_dict["claimedAt"] = claimed_at
        if operation_allowed is not UNSET:
            field_dict["operationAllowed"] = operation_allowed
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if exact is not UNSET:
            field_dict["exact"] = exact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_punchout_claimed_additional_property_exact import (
            PurchaseOrderPunchoutClaimedAdditionalPropertyExact,
        )

        d = src_dict.copy()
        claim_floor = d.pop("claimFloor", UNSET)

        claimed_at = d.pop("claimedAt", UNSET)

        _operation_allowed = d.pop("operationAllowed", UNSET)
        operation_allowed: Union[
            Unset, PurchaseOrderPunchoutClaimedAdditionalPropertyOperationAllowed
        ]
        if isinstance(_operation_allowed, Unset):
            operation_allowed = UNSET
        else:
            operation_allowed = check_purchase_order_punchout_claimed_additional_property_operation_allowed(
                _operation_allowed
            )

        order_by = d.pop("orderBy", UNSET)

        _exact = d.pop("exact", UNSET)
        exact: Union[Unset, PurchaseOrderPunchoutClaimedAdditionalPropertyExact]
        if isinstance(_exact, Unset):
            exact = UNSET
        else:
            exact = PurchaseOrderPunchoutClaimedAdditionalPropertyExact.from_dict(
                _exact
            )

        purchase_order_punchout_claimed_additional_property = cls(
            claim_floor=claim_floor,
            claimed_at=claimed_at,
            operation_allowed=operation_allowed,
            order_by=order_by,
            exact=exact,
        )

        purchase_order_punchout_claimed_additional_property.additional_properties = d
        return purchase_order_punchout_claimed_additional_property

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
