from typing import Literal, Set, cast

AiSavingRecommendationKind = Literal["batch", "cache", "reserve"]

AI_SAVING_RECOMMENDATION_KIND_VALUES: Set[AiSavingRecommendationKind] = {
    "batch",
    "cache",
    "reserve",
}


def check_ai_saving_recommendation_kind(value: str) -> AiSavingRecommendationKind:
    if value in AI_SAVING_RECOMMENDATION_KIND_VALUES:
        return cast(AiSavingRecommendationKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SAVING_RECOMMENDATION_KIND_VALUES!r}"
    )
