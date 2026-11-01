from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_invoice_total_by_category import FocusInvoiceTotalByCategory
    from ..models.focus_invoice_total_by_service import FocusInvoiceTotalByService


T = TypeVar("T", bound="FocusInvoiceTotal")


@_attrs_define
class FocusInvoiceTotal:
    """
    Attributes:
        issuer (Union[Unset, str]):
        billing_account_id (Union[Unset, str]):
        invoice_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        total (Union[Unset, float]):
        by_category (Union[Unset, FocusInvoiceTotalByCategory]):
        by_service (Union[Unset, FocusInvoiceTotalByService]):
        corrections (Union[Unset, float]):
    """

    issuer: Union[Unset, str] = UNSET
    billing_account_id: Union[Unset, str] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    by_category: Union[Unset, "FocusInvoiceTotalByCategory"] = UNSET
    by_service: Union[Unset, "FocusInvoiceTotalByService"] = UNSET
    corrections: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer = self.issuer

        billing_account_id = self.billing_account_id

        invoice_id = self.invoice_id

        currency = self.currency

        total = self.total

        by_category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_category, Unset):
            by_category = self.by_category.to_dict()

        by_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_service, Unset):
            by_service = self.by_service.to_dict()

        corrections = self.corrections

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if billing_account_id is not UNSET:
            field_dict["billingAccountId"] = billing_account_id
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total is not UNSET:
            field_dict["total"] = total
        if by_category is not UNSET:
            field_dict["byCategory"] = by_category
        if by_service is not UNSET:
            field_dict["byService"] = by_service
        if corrections is not UNSET:
            field_dict["corrections"] = corrections

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_invoice_total_by_category import FocusInvoiceTotalByCategory
        from ..models.focus_invoice_total_by_service import FocusInvoiceTotalByService

        d = src_dict.copy()
        issuer = d.pop("issuer", UNSET)

        billing_account_id = d.pop("billingAccountId", UNSET)

        invoice_id = d.pop("invoiceId", UNSET)

        currency = d.pop("currency", UNSET)

        total = d.pop("total", UNSET)

        _by_category = d.pop("byCategory", UNSET)
        by_category: Union[Unset, FocusInvoiceTotalByCategory]
        if isinstance(_by_category, Unset):
            by_category = UNSET
        else:
            by_category = FocusInvoiceTotalByCategory.from_dict(_by_category)

        _by_service = d.pop("byService", UNSET)
        by_service: Union[Unset, FocusInvoiceTotalByService]
        if isinstance(_by_service, Unset):
            by_service = UNSET
        else:
            by_service = FocusInvoiceTotalByService.from_dict(_by_service)

        corrections = d.pop("corrections", UNSET)

        focus_invoice_total = cls(
            issuer=issuer,
            billing_account_id=billing_account_id,
            invoice_id=invoice_id,
            currency=currency,
            total=total,
            by_category=by_category,
            by_service=by_service,
            corrections=corrections,
        )

        focus_invoice_total.additional_properties = d
        return focus_invoice_total

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
