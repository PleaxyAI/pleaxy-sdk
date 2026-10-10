from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automation_rule_set_view import AutomationRuleSetView
from ...types import Response


def _get_kwargs(
    process: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/automation-rules/{process}".format(
            process=process,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AutomationRuleSetView]:
    if response.status_code == 200:
        response_200 = AutomationRuleSetView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AutomationRuleSetView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AutomationRuleSetView]:
    """[Buyer] Get the configured automation rules for a process, and whether the plan lets auto-approve
    rules run

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationRuleSetView]
    """

    kwargs = _get_kwargs(
        process=process,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AutomationRuleSetView]:
    """[Buyer] Get the configured automation rules for a process, and whether the plan lets auto-approve
    rules run

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationRuleSetView
    """

    return sync_detailed(
        process=process,
        client=client,
    ).parsed


async def asyncio_detailed(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AutomationRuleSetView]:
    """[Buyer] Get the configured automation rules for a process, and whether the plan lets auto-approve
    rules run

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationRuleSetView]
    """

    kwargs = _get_kwargs(
        process=process,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AutomationRuleSetView]:
    """[Buyer] Get the configured automation rules for a process, and whether the plan lets auto-approve
    rules run

    Args:
        process (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationRuleSetView
    """

    return (
        await asyncio_detailed(
            process=process,
            client=client,
        )
    ).parsed
