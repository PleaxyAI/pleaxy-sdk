from typing import (
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """
    Attributes:
        status_code (int): The HTTP status, repeated.
        message (Union[List[str], str]): What went wrong, for a person; one entry per problem when the body failed
            validation.
        code (Union[Unset, str]): A stable, machine-readable reason, when the API names one - e.g. PO_ID_AMBIGUOUS.
        error (Union[Unset, str]): The status text, e.g. Bad Request.
    """

    status_code: int
    message: Union[List[str], str]
    code: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code

        message: Union[List[str], str]
        if isinstance(self.message, list):
            message = self.message

        else:
            message = self.message

        code = self.code

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statusCode": status_code,
                "message": message,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("statusCode")

        def _parse_message(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                message_type_1 = cast(List[str], data)

                return message_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        message = _parse_message(d.pop("message"))

        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        api_error = cls(
            status_code=status_code,
            message=message,
            code=code,
            error=error,
        )

        api_error.additional_properties = d
        return api_error

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
