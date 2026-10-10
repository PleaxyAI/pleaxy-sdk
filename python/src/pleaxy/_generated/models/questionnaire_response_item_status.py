from typing import Literal, Set, cast

QuestionnaireResponseItemStatus = Literal[
    "auto_filled", "manual", "missing", "not_applicable"
]

QUESTIONNAIRE_RESPONSE_ITEM_STATUS_VALUES: Set[QuestionnaireResponseItemStatus] = {
    "auto_filled",
    "manual",
    "missing",
    "not_applicable",
}


def check_questionnaire_response_item_status(
    value: str,
) -> QuestionnaireResponseItemStatus:
    if value in QUESTIONNAIRE_RESPONSE_ITEM_STATUS_VALUES:
        return cast(QuestionnaireResponseItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUESTIONNAIRE_RESPONSE_ITEM_STATUS_VALUES!r}"
    )
