from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0 import (
        InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0,
    )
    from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_1 import (
        InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1,
    )
    from ..models.invoice_counterparty_open_purchase_orders_item_lines_item import (
        InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem,
    )
    from ..models.open_purchase_order_deposit import OpenPurchaseOrderDeposit


T = TypeVar("T", bound="InvoiceCounterpartyOpenPurchaseOrdersItem")


@_attrs_define
class InvoiceCounterpartyOpenPurchaseOrdersItem:
    """
    Attributes:
        id (str):
        amount (Union[Unset, float]):
        created_at (Union[Unset, str]):
        label (Union[Unset, str]):
        currency (Union[Unset, str]):
        invoiced_amount (Union[Unset, float]):
        lines (Union[Unset, List['InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem']]):
        default_due_in_days (Union[Unset, float]):
        default_due_rule (Union['InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0',
            'InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1', Unset]):
        bill_to_company_name (Union[Unset, str]):
        paid_deposits (Union[Unset, List['OpenPurchaseOrderDeposit']]):
    """

    id: str
    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    invoiced_amount: Union[Unset, float] = UNSET
    lines: Union[Unset, List["InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem"]] = (
        UNSET
    )
    default_due_in_days: Union[Unset, float] = UNSET
    default_due_rule: Union[
        "InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0",
        "InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1",
        Unset,
    ] = UNSET
    bill_to_company_name: Union[Unset, str] = UNSET
    paid_deposits: Union[Unset, List["OpenPurchaseOrderDeposit"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0 import (
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0,
        )

        id = self.id

        amount = self.amount

        created_at = self.created_at

        label = self.label

        currency = self.currency

        invoiced_amount = self.invoiced_amount

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        default_due_in_days = self.default_due_in_days

        default_due_rule: Union[Dict[str, Any], Unset]
        if isinstance(self.default_due_rule, Unset):
            default_due_rule = UNSET
        elif isinstance(
            self.default_due_rule,
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0,
        ):
            default_due_rule = self.default_due_rule.to_dict()
        else:
            default_due_rule = self.default_due_rule.to_dict()

        bill_to_company_name = self.bill_to_company_name

        paid_deposits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.paid_deposits, Unset):
            paid_deposits = []
            for paid_deposits_item_data in self.paid_deposits:
                paid_deposits_item = paid_deposits_item_data.to_dict()
                paid_deposits.append(paid_deposits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if label is not UNSET:
            field_dict["label"] = label
        if currency is not UNSET:
            field_dict["currency"] = currency
        if invoiced_amount is not UNSET:
            field_dict["invoicedAmount"] = invoiced_amount
        if lines is not UNSET:
            field_dict["lines"] = lines
        if default_due_in_days is not UNSET:
            field_dict["defaultDueInDays"] = default_due_in_days
        if default_due_rule is not UNSET:
            field_dict["defaultDueRule"] = default_due_rule
        if bill_to_company_name is not UNSET:
            field_dict["billToCompanyName"] = bill_to_company_name
        if paid_deposits is not UNSET:
            field_dict["paidDeposits"] = paid_deposits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0 import (
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0,
        )
        from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_1 import (
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1,
        )
        from ..models.invoice_counterparty_open_purchase_orders_item_lines_item import (
            InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem,
        )
        from ..models.open_purchase_order_deposit import OpenPurchaseOrderDeposit

        d = src_dict.copy()
        id = d.pop("id")

        amount = d.pop("amount", UNSET)

        created_at = d.pop("createdAt", UNSET)

        label = d.pop("label", UNSET)

        currency = d.pop("currency", UNSET)

        invoiced_amount = d.pop("invoicedAmount", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem.from_dict(
                lines_item_data
            )

            lines.append(lines_item)

        default_due_in_days = d.pop("defaultDueInDays", UNSET)

        def _parse_default_due_rule(
            data: object,
        ) -> Union[
            "InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0",
            "InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_due_rule_type_0 = InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0.from_dict(
                    data
                )

                return default_due_rule_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            default_due_rule_type_1 = (
                InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1.from_dict(
                    data
                )
            )

            return default_due_rule_type_1

        default_due_rule = _parse_default_due_rule(d.pop("defaultDueRule", UNSET))

        bill_to_company_name = d.pop("billToCompanyName", UNSET)

        paid_deposits = []
        _paid_deposits = d.pop("paidDeposits", UNSET)
        for paid_deposits_item_data in _paid_deposits or []:
            paid_deposits_item = OpenPurchaseOrderDeposit.from_dict(
                paid_deposits_item_data
            )

            paid_deposits.append(paid_deposits_item)

        invoice_counterparty_open_purchase_orders_item = cls(
            id=id,
            amount=amount,
            created_at=created_at,
            label=label,
            currency=currency,
            invoiced_amount=invoiced_amount,
            lines=lines,
            default_due_in_days=default_due_in_days,
            default_due_rule=default_due_rule,
            bill_to_company_name=bill_to_company_name,
            paid_deposits=paid_deposits,
        )

        invoice_counterparty_open_purchase_orders_item.additional_properties = d
        return invoice_counterparty_open_purchase_orders_item

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
