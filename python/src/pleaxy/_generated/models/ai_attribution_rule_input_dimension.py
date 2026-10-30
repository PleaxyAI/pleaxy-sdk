from typing import Literal, Set, cast

AiAttributionRuleInputDimension = Literal[
    "api_key",
    "cluster",
    "compartment",
    "inference_profile",
    "label",
    "project",
    "resource_group",
    "tag",
    "workspace",
]

AI_ATTRIBUTION_RULE_INPUT_DIMENSION_VALUES: Set[AiAttributionRuleInputDimension] = {
    "api_key",
    "cluster",
    "compartment",
    "inference_profile",
    "label",
    "project",
    "resource_group",
    "tag",
    "workspace",
}


def check_ai_attribution_rule_input_dimension(
    value: str,
) -> AiAttributionRuleInputDimension:
    if value in AI_ATTRIBUTION_RULE_INPUT_DIMENSION_VALUES:
        return cast(AiAttributionRuleInputDimension, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_ATTRIBUTION_RULE_INPUT_DIMENSION_VALUES!r}"
    )
