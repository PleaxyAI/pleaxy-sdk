from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_request_line_input import PurchaseRequestLineInput
    from ..models.purchase_request_supplier_input import PurchaseRequestSupplierInput


T = TypeVar("T", bound="UpdatePurchaseRequestInput")


@_attrs_define
class UpdatePurchaseRequestInput:
    """
    Attributes:
        title (Union[Unset, str]): What is needed, in a few words.
        description (Union[Unset, str]): Why it is needed: the business reason. Required to submit.
        cost_center (Union[Unset, str]): The cost center (a code or name on the workspace's list, stored as its code).
            Required to submit when the workspace keeps a list.
        gl_code (Union[Unset, str]): The GL account (spend category), when it isn't the cost center's.
        supplier (Union[Unset, PurchaseRequestSupplierInput]):
        line_items (Union[Unset, List['PurchaseRequestLineInput']]): What is needed, line by line (one line is fine for
            an estimate).
        currency (Union[Unset, str]): ISO 4217; the workspace's currency when absent.
        needed_by (Union[Unset, str]): When it's needed, YYYY-MM-DD.
        quote_import_id (Union[Unset, str]): A quote uploaded through the quote import, to attach.
        notes (Union[Unset, str]): Anything procurement should know.
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    supplier: Union[Unset, "PurchaseRequestSupplierInput"] = UNSET
    line_items: Union[Unset, List["PurchaseRequestLineInput"]] = UNSET
    currency: Union[Unset, str] = UNSET
    needed_by: Union[Unset, str] = UNSET
    quote_import_id: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        description = self.description

        cost_center = self.cost_center

        gl_code = self.gl_code

        supplier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier, Unset):
            supplier = self.supplier.to_dict()

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        currency = self.currency

        needed_by = self.needed_by

        quote_import_id = self.quote_import_id

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if currency is not UNSET:
            field_dict["currency"] = currency
        if needed_by is not UNSET:
            field_dict["neededBy"] = needed_by
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_request_line_input import PurchaseRequestLineInput
        from ..models.purchase_request_supplier_input import (
            PurchaseRequestSupplierInput,
        )

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        gl_code = d.pop("glCode", UNSET)

        _supplier = d.pop("supplier", UNSET)
        supplier: Union[Unset, PurchaseRequestSupplierInput]
        if isinstance(_supplier, Unset):
            supplier = UNSET
        else:
            supplier = PurchaseRequestSupplierInput.from_dict(_supplier)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = PurchaseRequestLineInput.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        currency = d.pop("currency", UNSET)

        needed_by = d.pop("neededBy", UNSET)

        quote_import_id = d.pop("quoteImportId", UNSET)

        notes = d.pop("notes", UNSET)

        update_purchase_request_input = cls(
            title=title,
            description=description,
            cost_center=cost_center,
            gl_code=gl_code,
            supplier=supplier,
            line_items=line_items,
            currency=currency,
            needed_by=needed_by,
            quote_import_id=quote_import_id,
            notes=notes,
        )

        update_purchase_request_input.additional_properties = d
        return update_purchase_request_input

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
