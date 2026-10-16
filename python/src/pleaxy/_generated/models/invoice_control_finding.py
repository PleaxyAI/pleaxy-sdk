from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_control_finding_code import (
    InvoiceControlFindingCode,
    check_invoice_control_finding_code,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_message_params import ServerMessageParams


T = TypeVar("T", bound="InvoiceControlFinding")


@_attrs_define
class InvoiceControlFinding:
    """
    Attributes:
        code (Union[Unset, InvoiceControlFindingCode]):
        message (Union[Unset, str]):
        message_id (Union[Unset, str]):
        params (Union[Unset, ServerMessageParams]):
        invoice_line (Union[Unset, float]):
        po_line_no (Union[Unset, float]):
        contract_id (Union[Unset, str]):
        allowed (Union[Unset, float]):
        billed (Union[Unset, float]):
        contract_version (Union[Unset, float]):
    """

    code: Union[Unset, InvoiceControlFindingCode] = UNSET
    message: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    params: Union[Unset, "ServerMessageParams"] = UNSET
    invoice_line: Union[Unset, float] = UNSET
    po_line_no: Union[Unset, float] = UNSET
    contract_id: Union[Unset, str] = UNSET
    allowed: Union[Unset, float] = UNSET
    billed: Union[Unset, float] = UNSET
    contract_version: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        message_id = self.message_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        invoice_line = self.invoice_line

        po_line_no = self.po_line_no

        contract_id = self.contract_id

        allowed = self.allowed

        billed = self.billed

        contract_version = self.contract_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if params is not UNSET:
            field_dict["params"] = params
        if invoice_line is not UNSET:
            field_dict["invoiceLine"] = invoice_line
        if po_line_no is not UNSET:
            field_dict["poLineNo"] = po_line_no
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if billed is not UNSET:
            field_dict["billed"] = billed
        if contract_version is not UNSET:
            field_dict["contractVersion"] = contract_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_message_params import ServerMessageParams

        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, InvoiceControlFindingCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_invoice_control_finding_code(_code)

        message = d.pop("message", UNSET)

        message_id = d.pop("messageId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ServerMessageParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ServerMessageParams.from_dict(_params)

        invoice_line = d.pop("invoiceLine", UNSET)

        po_line_no = d.pop("poLineNo", UNSET)

        contract_id = d.pop("contractId", UNSET)

        allowed = d.pop("allowed", UNSET)

        billed = d.pop("billed", UNSET)

        contract_version = d.pop("contractVersion", UNSET)

        invoice_control_finding = cls(
            code=code,
            message=message,
            message_id=message_id,
            params=params,
            invoice_line=invoice_line,
            po_line_no=po_line_no,
            contract_id=contract_id,
            allowed=allowed,
            billed=billed,
            contract_version=contract_version,
        )

        invoice_control_finding.additional_properties = d
        return invoice_control_finding

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
