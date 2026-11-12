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
    from ..models.buyer_credit_note_view import BuyerCreditNoteView
    from ..models.supplier_credit_note_view import SupplierCreditNoteView


T = TypeVar("T", bound="ListCreditNotesResult")


@_attrs_define
class ListCreditNotesResult:
    """
    Attributes:
        credit_notes (Union[Unset, List[Union['BuyerCreditNoteView', 'SupplierCreditNoteView']]]):
    """

    credit_notes: Union[
        Unset, List[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.supplier_credit_note_view import SupplierCreditNoteView

        credit_notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credit_notes, Unset):
            credit_notes = []
            for credit_notes_item_data in self.credit_notes:
                credit_notes_item: Dict[str, Any]
                if isinstance(credit_notes_item_data, SupplierCreditNoteView):
                    credit_notes_item = credit_notes_item_data.to_dict()
                else:
                    credit_notes_item = credit_notes_item_data.to_dict()

                credit_notes.append(credit_notes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_notes is not UNSET:
            field_dict["creditNotes"] = credit_notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.buyer_credit_note_view import BuyerCreditNoteView
        from ..models.supplier_credit_note_view import SupplierCreditNoteView

        d = src_dict.copy()
        credit_notes = []
        _credit_notes = d.pop("creditNotes", UNSET)
        for credit_notes_item_data in _credit_notes or []:

            def _parse_credit_notes_item(
                data: object,
            ) -> Union["BuyerCreditNoteView", "SupplierCreditNoteView"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    credit_notes_item_type_0 = SupplierCreditNoteView.from_dict(data)

                    return credit_notes_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                credit_notes_item_type_1 = BuyerCreditNoteView.from_dict(data)

                return credit_notes_item_type_1

            credit_notes_item = _parse_credit_notes_item(credit_notes_item_data)

            credit_notes.append(credit_notes_item)

        list_credit_notes_result = cls(
            credit_notes=credit_notes,
        )

        list_credit_notes_result.additional_properties = d
        return list_credit_notes_result

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
