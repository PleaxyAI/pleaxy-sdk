from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_key_input_procurement_role import (
    CreateApiKeyInputProcurementRole,
    check_create_api_key_input_procurement_role,
)
from ..models.create_api_key_input_scopes_item import (
    CreateApiKeyInputScopesItem,
    check_create_api_key_input_scopes_item,
)
from ..models.create_api_key_input_supplier_role import (
    CreateApiKeyInputSupplierRole,
    check_create_api_key_input_supplier_role,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApiKeyInput")


@_attrs_define
class CreateApiKeyInput:
    """
    Attributes:
        label (str): Human-readable label, e.g. "Billing agent - prod"
        procurement_role (Union[Unset, CreateApiKeyInputProcurementRole]): Buyer-side procurement authority the key
            grants. Defaults to `read-only`. `agent` is for an AI agent or integration that raises purchase orders and
            enters invoices: it reads contracts, suppliers and questionnaires, and changes no approval rule, auto-approval
            or billing. Minting requires `edit` on `approvalSettings` (i.e. an administrator). Ignored for supplier-side
            keys.
        supplier_role (Union[Unset, CreateApiKeyInputSupplierRole]): Supplier-side keys: the role the key acts with, as
            people have - administrator, accounts-receivable, sales, fulfillment or read-only. Defaults to `read-only`.
            invoices:feed needs a role that edits invoices (administrator, accounts-receivable); orders:fulfill one that
            edits orders (administrator, fulfillment). Ignored for buyer-side keys.
        scopes (Union[Unset, List[CreateApiKeyInputScopesItem]]): Extra abilities, each for one side (the other side's
            scope is a 400). Supplier: `invoices:feed` lets the key submit invoices to a connected buyer through POST
            .../invoices/connections/:connectionId; `orders:fulfill` lets it confirm orders and send ship notices, through
            POST .../purchase-orders/:poId/confirmations and .../ship-notices or as cXML to POST /v1/cxml/fulfillment.
            Buyer: `payments:record` lets the key record payments made outside Pleaxy through POST .../invoices/payment-
            records, and needs a procurementRole that can edit invoices. A scoped key keeps every other ability of its side.
            Only an administrator can mint a scoped key.
    """

    label: str
    procurement_role: Union[Unset, CreateApiKeyInputProcurementRole] = UNSET
    supplier_role: Union[Unset, CreateApiKeyInputSupplierRole] = UNSET
    scopes: Union[Unset, List[CreateApiKeyInputScopesItem]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        procurement_role: Union[Unset, str] = UNSET
        if not isinstance(self.procurement_role, Unset):
            procurement_role = self.procurement_role

        supplier_role: Union[Unset, str] = UNSET
        if not isinstance(self.supplier_role, Unset):
            supplier_role = self.supplier_role

        scopes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item: str = scopes_item_data
                scopes.append(scopes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if procurement_role is not UNSET:
            field_dict["procurementRole"] = procurement_role
        if supplier_role is not UNSET:
            field_dict["supplierRole"] = supplier_role
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        _procurement_role = d.pop("procurementRole", UNSET)
        procurement_role: Union[Unset, CreateApiKeyInputProcurementRole]
        if isinstance(_procurement_role, Unset):
            procurement_role = UNSET
        else:
            procurement_role = check_create_api_key_input_procurement_role(
                _procurement_role
            )

        _supplier_role = d.pop("supplierRole", UNSET)
        supplier_role: Union[Unset, CreateApiKeyInputSupplierRole]
        if isinstance(_supplier_role, Unset):
            supplier_role = UNSET
        else:
            supplier_role = check_create_api_key_input_supplier_role(_supplier_role)

        scopes = []
        _scopes = d.pop("scopes", UNSET)
        for scopes_item_data in _scopes or []:
            scopes_item = check_create_api_key_input_scopes_item(scopes_item_data)

            scopes.append(scopes_item)

        create_api_key_input = cls(
            label=label,
            procurement_role=procurement_role,
            supplier_role=supplier_role,
            scopes=scopes,
        )

        create_api_key_input.additional_properties = d
        return create_api_key_input

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
