from typing import Literal, Set, cast

QuestionnaireFieldDefDocType = Literal[
    "bank_letter", "business_license", "coi", "w8ben", "w9"
]

QUESTIONNAIRE_FIELD_DEF_DOC_TYPE_VALUES: Set[QuestionnaireFieldDefDocType] = {
    "bank_letter",
    "business_license",
    "coi",
    "w8ben",
    "w9",
}


def check_questionnaire_field_def_doc_type(value: str) -> QuestionnaireFieldDefDocType:
    if value in QUESTIONNAIRE_FIELD_DEF_DOC_TYPE_VALUES:
        return cast(QuestionnaireFieldDefDocType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUESTIONNAIRE_FIELD_DEF_DOC_TYPE_VALUES!r}"
    )
