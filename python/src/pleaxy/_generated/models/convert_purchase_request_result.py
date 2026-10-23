from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order import PurchaseOrder
    from ..models.purchase_request import PurchaseRequest


T = TypeVar("T", bound="ConvertPurchaseRequestResult")


@_attrs_define
class ConvertPurchaseRequestResult:
    """
    Attributes:
        request (Union[Unset, PurchaseRequest]):
        purchase_order (Union[Unset, PurchaseOrder]):
    """

    request: Union[Unset, "PurchaseRequest"] = UNSET
    purchase_order: Union[Unset, "PurchaseOrder"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        purchase_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order, Unset):
            purchase_order = self.purchase_order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if purchase_order is not UNSET:
            field_dict["purchaseOrder"] = purchase_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order import PurchaseOrder
        from ..models.purchase_request import PurchaseRequest

        d = src_dict.copy()
        _request = d.pop("request", UNSET)
        request: Union[Unset, PurchaseRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = PurchaseRequest.from_dict(_request)

        _purchase_order = d.pop("purchaseOrder", UNSET)
        purchase_order: Union[Unset, PurchaseOrder]
        if isinstance(_purchase_order, Unset):
            purchase_order = UNSET
        else:
            purchase_order = PurchaseOrder.from_dict(_purchase_order)

        convert_purchase_request_result = cls(
            request=request,
            purchase_order=purchase_order,
        )

        convert_purchase_request_result.additional_properties = d
        return convert_purchase_request_result

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
