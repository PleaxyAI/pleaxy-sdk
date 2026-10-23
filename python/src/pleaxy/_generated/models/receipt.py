from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.receipt_kind import ReceiptKind, check_receipt_kind
from ..models.receipt_source import ReceiptSource, check_receipt_source
from ..models.receipt_status import ReceiptStatus, check_receipt_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain import ApprovalChain
    from ..models.receipt_attachment import ReceiptAttachment
    from ..models.receipt_line import ReceiptLine
    from ..models.receipt_rejection import ReceiptRejection
    from ..models.receipt_return import ReceiptReturn
    from ..models.receipt_reversal import ReceiptReversal


T = TypeVar("T", bound="Receipt")


@_attrs_define
class Receipt:
    """
    Attributes:
        id (str):
        po_id (Union[Unset, str]):
        kind (Union[Unset, ReceiptKind]):
        status (Union[Unset, ReceiptStatus]):
        received_at (Union[Unset, str]):
        period_from (Union[Unset, str]):
        period_to (Union[Unset, str]):
        lines (Union[Unset, List['ReceiptLine']]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        note (Union[Unset, str]):
        attachment (Union[Unset, ReceiptAttachment]):
        source (Union[Unset, ReceiptSource]):
        created_by (Union[Unset, str]):
        created_by_name (Union[Unset, str]):
        created_at (Union[Unset, str]):
        approved_by (Union[Unset, str]):
        approved_by_name (Union[Unset, str]):
        approved_at (Union[Unset, str]):
        reversal (Union[Unset, ReceiptReversal]):
        approval (Union[Unset, ApprovalChain]):
        approval_version (Union[Unset, float]):
        rejection (Union[Unset, ReceiptRejection]):
        returns (Union[Unset, List['ReceiptReturn']]):
    """

    id: str
    po_id: Union[Unset, str] = UNSET
    kind: Union[Unset, ReceiptKind] = UNSET
    status: Union[Unset, ReceiptStatus] = UNSET
    received_at: Union[Unset, str] = UNSET
    period_from: Union[Unset, str] = UNSET
    period_to: Union[Unset, str] = UNSET
    lines: Union[Unset, List["ReceiptLine"]] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    attachment: Union[Unset, "ReceiptAttachment"] = UNSET
    source: Union[Unset, ReceiptSource] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_by_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    approved_by: Union[Unset, str] = UNSET
    approved_by_name: Union[Unset, str] = UNSET
    approved_at: Union[Unset, str] = UNSET
    reversal: Union[Unset, "ReceiptReversal"] = UNSET
    approval: Union[Unset, "ApprovalChain"] = UNSET
    approval_version: Union[Unset, float] = UNSET
    rejection: Union[Unset, "ReceiptRejection"] = UNSET
    returns: Union[Unset, List["ReceiptReturn"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        po_id = self.po_id

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        received_at = self.received_at

        period_from = self.period_from

        period_to = self.period_to

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        amount = self.amount

        currency = self.currency

        note = self.note

        attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        created_by = self.created_by

        created_by_name = self.created_by_name

        created_at = self.created_at

        approved_by = self.approved_by

        approved_by_name = self.approved_by_name

        approved_at = self.approved_at

        reversal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reversal, Unset):
            reversal = self.reversal.to_dict()

        approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        approval_version = self.approval_version

        rejection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()

        returns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.returns, Unset):
            returns = []
            for returns_item_data in self.returns:
                returns_item = returns_item_data.to_dict()
                returns.append(returns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at
        if period_from is not UNSET:
            field_dict["periodFrom"] = period_from
        if period_to is not UNSET:
            field_dict["periodTo"] = period_to
        if lines is not UNSET:
            field_dict["lines"] = lines
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if note is not UNSET:
            field_dict["note"] = note
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if source is not UNSET:
            field_dict["source"] = source
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if approved_by_name is not UNSET:
            field_dict["approvedByName"] = approved_by_name
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if reversal is not UNSET:
            field_dict["reversal"] = reversal
        if approval is not UNSET:
            field_dict["approval"] = approval
        if approval_version is not UNSET:
            field_dict["approvalVersion"] = approval_version
        if rejection is not UNSET:
            field_dict["rejection"] = rejection
        if returns is not UNSET:
            field_dict["returns"] = returns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain import ApprovalChain
        from ..models.receipt_attachment import ReceiptAttachment
        from ..models.receipt_line import ReceiptLine
        from ..models.receipt_rejection import ReceiptRejection
        from ..models.receipt_return import ReceiptReturn
        from ..models.receipt_reversal import ReceiptReversal

        d = src_dict.copy()
        id = d.pop("id")

        po_id = d.pop("poId", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ReceiptKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_receipt_kind(_kind)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReceiptStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_receipt_status(_status)

        received_at = d.pop("receivedAt", UNSET)

        period_from = d.pop("periodFrom", UNSET)

        period_to = d.pop("periodTo", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ReceiptLine.from_dict(lines_item_data)

            lines.append(lines_item)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        note = d.pop("note", UNSET)

        _attachment = d.pop("attachment", UNSET)
        attachment: Union[Unset, ReceiptAttachment]
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = ReceiptAttachment.from_dict(_attachment)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ReceiptSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_receipt_source(_source)

        created_by = d.pop("createdBy", UNSET)

        created_by_name = d.pop("createdByName", UNSET)

        created_at = d.pop("createdAt", UNSET)

        approved_by = d.pop("approvedBy", UNSET)

        approved_by_name = d.pop("approvedByName", UNSET)

        approved_at = d.pop("approvedAt", UNSET)

        _reversal = d.pop("reversal", UNSET)
        reversal: Union[Unset, ReceiptReversal]
        if isinstance(_reversal, Unset):
            reversal = UNSET
        else:
            reversal = ReceiptReversal.from_dict(_reversal)

        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, ApprovalChain]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = ApprovalChain.from_dict(_approval)

        approval_version = d.pop("approvalVersion", UNSET)

        _rejection = d.pop("rejection", UNSET)
        rejection: Union[Unset, ReceiptRejection]
        if isinstance(_rejection, Unset):
            rejection = UNSET
        else:
            rejection = ReceiptRejection.from_dict(_rejection)

        returns = []
        _returns = d.pop("returns", UNSET)
        for returns_item_data in _returns or []:
            returns_item = ReceiptReturn.from_dict(returns_item_data)

            returns.append(returns_item)

        receipt = cls(
            id=id,
            po_id=po_id,
            kind=kind,
            status=status,
            received_at=received_at,
            period_from=period_from,
            period_to=period_to,
            lines=lines,
            amount=amount,
            currency=currency,
            note=note,
            attachment=attachment,
            source=source,
            created_by=created_by,
            created_by_name=created_by_name,
            created_at=created_at,
            approved_by=approved_by,
            approved_by_name=approved_by_name,
            approved_at=approved_at,
            reversal=reversal,
            approval=approval,
            approval_version=approval_version,
            rejection=rejection,
            returns=returns,
        )

        receipt.additional_properties = d
        return receipt

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
