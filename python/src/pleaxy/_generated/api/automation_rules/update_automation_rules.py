from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automation_rule_set import AutomationRuleSet
from ...models.update_automation_rules_input import UpdateAutomationRulesInput
from ...types import Response


def _get_kwargs(
    process: str,
    *,
    body: UpdateAutomationRulesInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/automation-rules/{process}".format(
            process=process,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AutomationRuleSet]:
    if response.status_code == 200:
        response_200 = AutomationRuleSet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AutomationRuleSet]:
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
    body: UpdateAutomationRulesInput,
) -> Response[AutomationRuleSet]:
    """[Buyer] Replace the automation rules for a process, in priority order. Needs a signed-in session;
    auto-approve rules need the Autonomous plan.

    Args:
        process (str):
        body (UpdateAutomationRulesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationRuleSet]
    """

    kwargs = _get_kwargs(
        process=process,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAutomationRulesInput,
) -> Optional[AutomationRuleSet]:
    """[Buyer] Replace the automation rules for a process, in priority order. Needs a signed-in session;
    auto-approve rules need the Autonomous plan.

    Args:
        process (str):
        body (UpdateAutomationRulesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationRuleSet
    """

    return sync_detailed(
        process=process,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAutomationRulesInput,
) -> Response[AutomationRuleSet]:
    """[Buyer] Replace the automation rules for a process, in priority order. Needs a signed-in session;
    auto-approve rules need the Autonomous plan.

    Args:
        process (str):
        body (UpdateAutomationRulesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationRuleSet]
    """

    kwargs = _get_kwargs(
        process=process,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAutomationRulesInput,
) -> Optional[AutomationRuleSet]:
    """[Buyer] Replace the automation rules for a process, in priority order. Needs a signed-in session;
    auto-approve rules need the Autonomous plan.

    Args:
        process (str):
        body (UpdateAutomationRulesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationRuleSet
    """

    return (
        await asyncio_detailed(
            process=process,
            client=client,
            body=body,
        )
    ).parsed
