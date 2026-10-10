from typing import Literal, Set, cast

QuestionnaireFieldDefKind = Literal["custom", "standard"]

QUESTIONNAIRE_FIELD_DEF_KIND_VALUES: Set[QuestionnaireFieldDefKind] = {
    "custom",
    "standard",
}


def check_questionnaire_field_def_kind(value: str) -> QuestionnaireFieldDefKind:
    if value in QUESTIONNAIRE_FIELD_DEF_KIND_VALUES:
        return cast(QuestionnaireFieldDefKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUESTIONNAIRE_FIELD_DEF_KIND_VALUES!r}"
    )
