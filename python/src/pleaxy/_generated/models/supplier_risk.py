from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_risk_level import SupplierRiskLevel, check_supplier_risk_level
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_risk_bank import SupplierRiskBank
    from ..models.supplier_risk_flagged_answers import SupplierRiskFlaggedAnswers
    from ..models.supplier_risk_missing_documents import SupplierRiskMissingDocuments
    from ..models.supplier_risk_screening import SupplierRiskScreening


T = TypeVar("T", bound="SupplierRisk")


@_attrs_define
class SupplierRisk:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        level (Union[Unset, SupplierRiskLevel]):
        bank (Union[Unset, SupplierRiskBank]):
        screening (Union[Unset, SupplierRiskScreening]):
        flagged_answers (Union[Unset, SupplierRiskFlaggedAnswers]):
        missing_documents (Union[Unset, SupplierRiskMissingDocuments]):
    """

    connection_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    level: Union[Unset, SupplierRiskLevel] = UNSET
    bank: Union[Unset, "SupplierRiskBank"] = UNSET
    screening: Union[Unset, "SupplierRiskScreening"] = UNSET
    flagged_answers: Union[Unset, "SupplierRiskFlaggedAnswers"] = UNSET
    missing_documents: Union[Unset, "SupplierRiskMissingDocuments"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id

        supplier_name = self.supplier_name

        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level

        bank: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bank, Unset):
            bank = self.bank.to_dict()

        screening: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.screening, Unset):
            screening = self.screening.to_dict()

        flagged_answers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flagged_answers, Unset):
            flagged_answers = self.flagged_answers.to_dict()

        missing_documents: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.missing_documents, Unset):
            missing_documents = self.missing_documents.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if level is not UNSET:
            field_dict["level"] = level
        if bank is not UNSET:
            field_dict["bank"] = bank
        if screening is not UNSET:
            field_dict["screening"] = screening
        if flagged_answers is not UNSET:
            field_dict["flaggedAnswers"] = flagged_answers
        if missing_documents is not UNSET:
            field_dict["missingDocuments"] = missing_documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_risk_bank import SupplierRiskBank
        from ..models.supplier_risk_flagged_answers import SupplierRiskFlaggedAnswers
        from ..models.supplier_risk_missing_documents import (
            SupplierRiskMissingDocuments,
        )
        from ..models.supplier_risk_screening import SupplierRiskScreening

        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, SupplierRiskLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = check_supplier_risk_level(_level)

        _bank = d.pop("bank", UNSET)
        bank: Union[Unset, SupplierRiskBank]
        if isinstance(_bank, Unset):
            bank = UNSET
        else:
            bank = SupplierRiskBank.from_dict(_bank)

        _screening = d.pop("screening", UNSET)
        screening: Union[Unset, SupplierRiskScreening]
        if isinstance(_screening, Unset):
            screening = UNSET
        else:
            screening = SupplierRiskScreening.from_dict(_screening)

        _flagged_answers = d.pop("flaggedAnswers", UNSET)
        flagged_answers: Union[Unset, SupplierRiskFlaggedAnswers]
        if isinstance(_flagged_answers, Unset):
            flagged_answers = UNSET
        else:
            flagged_answers = SupplierRiskFlaggedAnswers.from_dict(_flagged_answers)

        _missing_documents = d.pop("missingDocuments", UNSET)
        missing_documents: Union[Unset, SupplierRiskMissingDocuments]
        if isinstance(_missing_documents, Unset):
            missing_documents = UNSET
        else:
            missing_documents = SupplierRiskMissingDocuments.from_dict(
                _missing_documents
            )

        supplier_risk = cls(
            connection_id=connection_id,
            supplier_name=supplier_name,
            level=level,
            bank=bank,
            screening=screening,
            flagged_answers=flagged_answers,
            missing_documents=missing_documents,
        )

        supplier_risk.additional_properties = d
        return supplier_risk

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
