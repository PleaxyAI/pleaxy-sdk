from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_renewal_rule import AiRenewalRule
from ...models.set_ai_renewal_rule_input import SetAiRenewalRuleInput
from ...types import Response


def _get_kwargs(
    *,
    body: SetAiRenewalRuleInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/ai-spend/renewal-rule",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiRenewalRule]:
    if response.status_code == 200:
        response_200 = AiRenewalRule.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiRenewalRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiRenewalRuleInput,
) -> Response[AiRenewalRule]:
    """[Buyer] Switches the renewal automation rule on or off: on or after dayOfMonth (1-28, default 25),
    once a month, Pleaxy drafts next month's order for each open order with AI lines, at the forecast,
    as the person who switched it on. With draftUncovered, it also drafts an order for this month's
    spend no order covers, once per provider or account a month, from the 3rd, and tells that person the
    drafts are ready. Drafts are never submitted: a person reviews them and they go through the usual
    approval. Logged-in users only, 'create' on purchase orders.

    Args:
        body (SetAiRenewalRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiRenewalRule]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiRenewalRuleInput,
) -> Optional[AiRenewalRule]:
    """[Buyer] Switches the renewal automation rule on or off: on or after dayOfMonth (1-28, default 25),
    once a month, Pleaxy drafts next month's order for each open order with AI lines, at the forecast,
    as the person who switched it on. With draftUncovered, it also drafts an order for this month's
    spend no order covers, once per provider or account a month, from the 3rd, and tells that person the
    drafts are ready. Drafts are never submitted: a person reviews them and they go through the usual
    approval. Logged-in users only, 'create' on purchase orders.

    Args:
        body (SetAiRenewalRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiRenewalRule
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiRenewalRuleInput,
) -> Response[AiRenewalRule]:
    """[Buyer] Switches the renewal automation rule on or off: on or after dayOfMonth (1-28, default 25),
    once a month, Pleaxy drafts next month's order for each open order with AI lines, at the forecast,
    as the person who switched it on. With draftUncovered, it also drafts an order for this month's
    spend no order covers, once per provider or account a month, from the 3rd, and tells that person the
    drafts are ready. Drafts are never submitted: a person reviews them and they go through the usual
    approval. Logged-in users only, 'create' on purchase orders.

    Args:
        body (SetAiRenewalRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiRenewalRule]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiRenewalRuleInput,
) -> Optional[AiRenewalRule]:
    """[Buyer] Switches the renewal automation rule on or off: on or after dayOfMonth (1-28, default 25),
    once a month, Pleaxy drafts next month's order for each open order with AI lines, at the forecast,
    as the person who switched it on. With draftUncovered, it also drafts an order for this month's
    spend no order covers, once per provider or account a month, from the 3rd, and tells that person the
    drafts are ready. Drafts are never submitted: a person reviews them and they go through the usual
    approval. Logged-in users only, 'create' on purchase orders.

    Args:
        body (SetAiRenewalRuleInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiRenewalRule
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
