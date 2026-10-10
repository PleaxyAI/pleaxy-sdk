from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_input import LineItemInput


T = TypeVar("T", bound="UpdatePurchaseOrderInput")


@_attrs_define
class UpdatePurchaseOrderInput:
    """
    Attributes:
        currency (Union[Unset, str]): Drafts only, sent with lineItems: the currency the order is priced in. To a
            supplier with an account, one it prices in; otherwise any ISO 4217 code. A submitted PO keeps its currency.
        line_items (Union[Unset, List['LineItemInput']]): Replaces the PO's whole line-item set and recalculates its
            amount. The approval chain is rebuilt from scratch, discarding any sign-offs already collected.
        bill_to (Union[Unset, str]):
        cost_center (Union[Unset, str]):
        budget_owner (Union[Unset, str]):
        buyer_name (Union[Unset, str]):
        notes (Union[Unset, str]):
        contract_id (Union[None, Unset, str]): The contract this order falls under - one of this workspace's, active,
            with the order's supplier (400 otherwise); `null` removes it. Bookkeeping: never re-triggers approval.
        quote_import_id (Union[None, Unset, str]): The quote import holding the supplier's quote this order is raised
            from; replaces the one attached, and `null` removes it. Bookkeeping, like `notes`.
    """

    currency: Union[Unset, str] = UNSET
    line_items: Union[Unset, List["LineItemInput"]] = UNSET
    bill_to: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    budget_owner: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    contract_id: Union[None, Unset, str] = UNSET
    quote_import_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        bill_to = self.bill_to

        cost_center = self.cost_center

        budget_owner = self.budget_owner

        buyer_name = self.buyer_name

        notes = self.notes

        contract_id: Union[None, Unset, str]
        if isinstance(self.contract_id, Unset):
            contract_id = UNSET
        else:
            contract_id = self.contract_id

        quote_import_id: Union[None, Unset, str]
        if isinstance(self.quote_import_id, Unset):
            quote_import_id = UNSET
        else:
            quote_import_id = self.quote_import_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if bill_to is not UNSET:
            field_dict["billTo"] = bill_to
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if budget_owner is not UNSET:
            field_dict["budgetOwner"] = budget_owner
        if buyer_name is not UNSET:
            field_dict["buyerName"] = buyer_name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_item_input import LineItemInput

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = LineItemInput.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        bill_to = d.pop("billTo", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        budget_owner = d.pop("budgetOwner", UNSET)

        buyer_name = d.pop("buyerName", UNSET)

        notes = d.pop("notes", UNSET)

        def _parse_contract_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contract_id = _parse_contract_id(d.pop("contractId", UNSET))

        def _parse_quote_import_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        quote_import_id = _parse_quote_import_id(d.pop("quoteImportId", UNSET))

        update_purchase_order_input = cls(
            currency=currency,
            line_items=line_items,
            bill_to=bill_to,
            cost_center=cost_center,
            budget_owner=budget_owner,
            buyer_name=buyer_name,
            notes=notes,
            contract_id=contract_id,
            quote_import_id=quote_import_id,
        )

        update_purchase_order_input.additional_properties = d
        return update_purchase_order_input

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
