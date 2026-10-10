from typing import Literal, Set, cast

QuestionnaireFieldDefType = Literal[
    "date",
    "file",
    "long_text",
    "multi_choice",
    "number",
    "single_choice",
    "text",
    "yes_no",
]

QUESTIONNAIRE_FIELD_DEF_TYPE_VALUES: Set[QuestionnaireFieldDefType] = {
    "date",
    "file",
    "long_text",
    "multi_choice",
    "number",
    "single_choice",
    "text",
    "yes_no",
}


def check_questionnaire_field_def_type(value: str) -> QuestionnaireFieldDefType:
    if value in QUESTIONNAIRE_FIELD_DEF_TYPE_VALUES:
        return cast(QuestionnaireFieldDefType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUESTIONNAIRE_FIELD_DEF_TYPE_VALUES!r}"
    )
