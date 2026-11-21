from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confluent_connection_input import ConfluentConnectionInput
    from ..models.credit_price_input import CreditPriceInput
    from ..models.databricks_connection_input import DatabricksConnectionInput
    from ..models.datadog_connection_input import DatadogConnectionInput
    from ..models.git_hub_connection_input import GitHubConnectionInput
    from ..models.mongo_db_connection_input import MongoDbConnectionInput
    from ..models.snowflake_connection_input import SnowflakeConnectionInput
    from ..models.twilio_connection_input import TwilioConnectionInput
    from ..models.vercel_connection_input import VercelConnectionInput
    from ..models.zoom_connection_input import ZoomConnectionInput


T = TypeVar("T", bound="CreateAiProviderInput")


@_attrs_define
class CreateAiProviderInput:
    """
    Attributes:
        provider (str):
        key (Union[Unset, str]):
        snowflake (Union[Unset, SnowflakeConnectionInput]):
        databricks (Union[Unset, DatabricksConnectionInput]):
        github (Union[Unset, GitHubConnectionInput]):
        zoom (Union[Unset, ZoomConnectionInput]):
        datadog (Union[Unset, DatadogConnectionInput]):
        twilio (Union[Unset, TwilioConnectionInput]):
        mongodb (Union[Unset, MongoDbConnectionInput]):
        confluent (Union[Unset, ConfluentConnectionInput]):
        vercel (Union[Unset, VercelConnectionInput]):
        credit_price (Union[Unset, CreditPriceInput]):
    """

    provider: str
    key: Union[Unset, str] = UNSET
    snowflake: Union[Unset, "SnowflakeConnectionInput"] = UNSET
    databricks: Union[Unset, "DatabricksConnectionInput"] = UNSET
    github: Union[Unset, "GitHubConnectionInput"] = UNSET
    zoom: Union[Unset, "ZoomConnectionInput"] = UNSET
    datadog: Union[Unset, "DatadogConnectionInput"] = UNSET
    twilio: Union[Unset, "TwilioConnectionInput"] = UNSET
    mongodb: Union[Unset, "MongoDbConnectionInput"] = UNSET
    confluent: Union[Unset, "ConfluentConnectionInput"] = UNSET
    vercel: Union[Unset, "VercelConnectionInput"] = UNSET
    credit_price: Union[Unset, "CreditPriceInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider

        key = self.key

        snowflake: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.snowflake, Unset):
            snowflake = self.snowflake.to_dict()

        databricks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.databricks, Unset):
            databricks = self.databricks.to_dict()

        github: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.github, Unset):
            github = self.github.to_dict()

        zoom: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.zoom, Unset):
            zoom = self.zoom.to_dict()

        datadog: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.datadog, Unset):
            datadog = self.datadog.to_dict()

        twilio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.twilio, Unset):
            twilio = self.twilio.to_dict()

        mongodb: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mongodb, Unset):
            mongodb = self.mongodb.to_dict()

        confluent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confluent, Unset):
            confluent = self.confluent.to_dict()

        vercel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vercel, Unset):
            vercel = self.vercel.to_dict()

        credit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_price, Unset):
            credit_price = self.credit_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if snowflake is not UNSET:
            field_dict["snowflake"] = snowflake
        if databricks is not UNSET:
            field_dict["databricks"] = databricks
        if github is not UNSET:
            field_dict["github"] = github
        if zoom is not UNSET:
            field_dict["zoom"] = zoom
        if datadog is not UNSET:
            field_dict["datadog"] = datadog
        if twilio is not UNSET:
            field_dict["twilio"] = twilio
        if mongodb is not UNSET:
            field_dict["mongodb"] = mongodb
        if confluent is not UNSET:
            field_dict["confluent"] = confluent
        if vercel is not UNSET:
            field_dict["vercel"] = vercel
        if credit_price is not UNSET:
            field_dict["creditPrice"] = credit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.confluent_connection_input import ConfluentConnectionInput
        from ..models.credit_price_input import CreditPriceInput
        from ..models.databricks_connection_input import DatabricksConnectionInput
        from ..models.datadog_connection_input import DatadogConnectionInput
        from ..models.git_hub_connection_input import GitHubConnectionInput
        from ..models.mongo_db_connection_input import MongoDbConnectionInput
        from ..models.snowflake_connection_input import SnowflakeConnectionInput
        from ..models.twilio_connection_input import TwilioConnectionInput
        from ..models.vercel_connection_input import VercelConnectionInput
        from ..models.zoom_connection_input import ZoomConnectionInput

        d = src_dict.copy()
        provider = d.pop("provider")

        key = d.pop("key", UNSET)

        _snowflake = d.pop("snowflake", UNSET)
        snowflake: Union[Unset, SnowflakeConnectionInput]
        if isinstance(_snowflake, Unset):
            snowflake = UNSET
        else:
            snowflake = SnowflakeConnectionInput.from_dict(_snowflake)

        _databricks = d.pop("databricks", UNSET)
        databricks: Union[Unset, DatabricksConnectionInput]
        if isinstance(_databricks, Unset):
            databricks = UNSET
        else:
            databricks = DatabricksConnectionInput.from_dict(_databricks)

        _github = d.pop("github", UNSET)
        github: Union[Unset, GitHubConnectionInput]
        if isinstance(_github, Unset):
            github = UNSET
        else:
            github = GitHubConnectionInput.from_dict(_github)

        _zoom = d.pop("zoom", UNSET)
        zoom: Union[Unset, ZoomConnectionInput]
        if isinstance(_zoom, Unset):
            zoom = UNSET
        else:
            zoom = ZoomConnectionInput.from_dict(_zoom)

        _datadog = d.pop("datadog", UNSET)
        datadog: Union[Unset, DatadogConnectionInput]
        if isinstance(_datadog, Unset):
            datadog = UNSET
        else:
            datadog = DatadogConnectionInput.from_dict(_datadog)

        _twilio = d.pop("twilio", UNSET)
        twilio: Union[Unset, TwilioConnectionInput]
        if isinstance(_twilio, Unset):
            twilio = UNSET
        else:
            twilio = TwilioConnectionInput.from_dict(_twilio)

        _mongodb = d.pop("mongodb", UNSET)
        mongodb: Union[Unset, MongoDbConnectionInput]
        if isinstance(_mongodb, Unset):
            mongodb = UNSET
        else:
            mongodb = MongoDbConnectionInput.from_dict(_mongodb)

        _confluent = d.pop("confluent", UNSET)
        confluent: Union[Unset, ConfluentConnectionInput]
        if isinstance(_confluent, Unset):
            confluent = UNSET
        else:
            confluent = ConfluentConnectionInput.from_dict(_confluent)

        _vercel = d.pop("vercel", UNSET)
        vercel: Union[Unset, VercelConnectionInput]
        if isinstance(_vercel, Unset):
            vercel = UNSET
        else:
            vercel = VercelConnectionInput.from_dict(_vercel)

        _credit_price = d.pop("creditPrice", UNSET)
        credit_price: Union[Unset, CreditPriceInput]
        if isinstance(_credit_price, Unset):
            credit_price = UNSET
        else:
            credit_price = CreditPriceInput.from_dict(_credit_price)

        create_ai_provider_input = cls(
            provider=provider,
            key=key,
            snowflake=snowflake,
            databricks=databricks,
            github=github,
            zoom=zoom,
            datadog=datadog,
            twilio=twilio,
            mongodb=mongodb,
            confluent=confluent,
            vercel=vercel,
            credit_price=credit_price,
        )

        create_ai_provider_input.additional_properties = d
        return create_ai_provider_input

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
