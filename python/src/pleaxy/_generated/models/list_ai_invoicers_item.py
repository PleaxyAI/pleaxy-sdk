from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_ai_invoicers_item_billing_item import (
    ListAiInvoicersItemBillingItem,
    check_list_ai_invoicers_item_billing_item,
)
from ..models.list_ai_invoicers_item_credential import (
    ListAiInvoicersItemCredential,
    check_list_ai_invoicers_item_credential,
)
from ..models.list_ai_invoicers_item_id import (
    ListAiInvoicersItemId,
    check_list_ai_invoicers_item_id,
)
from ..models.list_ai_invoicers_item_shape import (
    ListAiInvoicersItemShape,
    check_list_ai_invoicers_item_shape,
)
from ..models.list_ai_invoicers_item_tier import (
    ListAiInvoicersItemTier,
    check_list_ai_invoicers_item_tier,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_ai_invoicers_item_legal_entities_item import (
        ListAiInvoicersItemLegalEntitiesItem,
    )


T = TypeVar("T", bound="ListAiInvoicersItem")


@_attrs_define
class ListAiInvoicersItem:
    """
    Attributes:
        id (ListAiInvoicersItemId):
        name (Union[Unset, str]):
        legal_entities (Union[Unset, List['ListAiInvoicersItemLegalEntitiesItem']]):
        billing_currencies (Union[Unset, List[str]]):
        billing (Union[Unset, List[ListAiInvoicersItemBillingItem]]):
        sender_domains (Union[Unset, List[str]]):
        credential (Union[Unset, ListAiInvoicersItemCredential]):
        tier (Union[Unset, ListAiInvoicersItemTier]):
        shape (Union[Unset, ListAiInvoicersItemShape]):
        contact_hint (Union[Unset, str]):
        connectable (Union[Unset, bool]):
    """

    id: ListAiInvoicersItemId
    name: Union[Unset, str] = UNSET
    legal_entities: Union[Unset, List["ListAiInvoicersItemLegalEntitiesItem"]] = UNSET
    billing_currencies: Union[Unset, List[str]] = UNSET
    billing: Union[Unset, List[ListAiInvoicersItemBillingItem]] = UNSET
    sender_domains: Union[Unset, List[str]] = UNSET
    credential: Union[Unset, ListAiInvoicersItemCredential] = UNSET
    tier: Union[Unset, ListAiInvoicersItemTier] = UNSET
    shape: Union[Unset, ListAiInvoicersItemShape] = UNSET
    contact_hint: Union[Unset, str] = UNSET
    connectable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id: str = self.id

        name = self.name

        legal_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.legal_entities, Unset):
            legal_entities = []
            for legal_entities_item_data in self.legal_entities:
                legal_entities_item = legal_entities_item_data.to_dict()
                legal_entities.append(legal_entities_item)

        billing_currencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.billing_currencies, Unset):
            billing_currencies = self.billing_currencies

        billing: Union[Unset, List[str]] = UNSET
        if not isinstance(self.billing, Unset):
            billing = []
            for billing_item_data in self.billing:
                billing_item: str = billing_item_data
                billing.append(billing_item)

        sender_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sender_domains, Unset):
            sender_domains = self.sender_domains

        credential: Union[Unset, str] = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential

        tier: Union[Unset, str] = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier

        shape: Union[Unset, str] = UNSET
        if not isinstance(self.shape, Unset):
            shape = self.shape

        contact_hint = self.contact_hint

        connectable = self.connectable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if legal_entities is not UNSET:
            field_dict["legalEntities"] = legal_entities
        if billing_currencies is not UNSET:
            field_dict["billingCurrencies"] = billing_currencies
        if billing is not UNSET:
            field_dict["billing"] = billing
        if sender_domains is not UNSET:
            field_dict["senderDomains"] = sender_domains
        if credential is not UNSET:
            field_dict["credential"] = credential
        if tier is not UNSET:
            field_dict["tier"] = tier
        if shape is not UNSET:
            field_dict["shape"] = shape
        if contact_hint is not UNSET:
            field_dict["contactHint"] = contact_hint
        if connectable is not UNSET:
            field_dict["connectable"] = connectable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_ai_invoicers_item_legal_entities_item import (
            ListAiInvoicersItemLegalEntitiesItem,
        )

        d = src_dict.copy()
        id = check_list_ai_invoicers_item_id(d.pop("id"))

        name = d.pop("name", UNSET)

        legal_entities = []
        _legal_entities = d.pop("legalEntities", UNSET)
        for legal_entities_item_data in _legal_entities or []:
            legal_entities_item = ListAiInvoicersItemLegalEntitiesItem.from_dict(
                legal_entities_item_data
            )

            legal_entities.append(legal_entities_item)

        billing_currencies = cast(List[str], d.pop("billingCurrencies", UNSET))

        billing = []
        _billing = d.pop("billing", UNSET)
        for billing_item_data in _billing or []:
            billing_item = check_list_ai_invoicers_item_billing_item(billing_item_data)

            billing.append(billing_item)

        sender_domains = cast(List[str], d.pop("senderDomains", UNSET))

        _credential = d.pop("credential", UNSET)
        credential: Union[Unset, ListAiInvoicersItemCredential]
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = check_list_ai_invoicers_item_credential(_credential)

        _tier = d.pop("tier", UNSET)
        tier: Union[Unset, ListAiInvoicersItemTier]
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = check_list_ai_invoicers_item_tier(_tier)

        _shape = d.pop("shape", UNSET)
        shape: Union[Unset, ListAiInvoicersItemShape]
        if isinstance(_shape, Unset):
            shape = UNSET
        else:
            shape = check_list_ai_invoicers_item_shape(_shape)

        contact_hint = d.pop("contactHint", UNSET)

        connectable = d.pop("connectable", UNSET)

        list_ai_invoicers_item = cls(
            id=id,
            name=name,
            legal_entities=legal_entities,
            billing_currencies=billing_currencies,
            billing=billing,
            sender_domains=sender_domains,
            credential=credential,
            tier=tier,
            shape=shape,
            contact_hint=contact_hint,
            connectable=connectable,
        )

        list_ai_invoicers_item.additional_properties = d
        return list_ai_invoicers_item

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
