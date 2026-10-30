from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_spend_limit import AiSpendLimit
from ...models.set_ai_spend_limit_input import SetAiSpendLimitInput
from ...types import Response


def _get_kwargs(
    po_id: str,
    line_no: float,
    *,
    body: SetAiSpendLimitInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/ai-spend/limits/{po_id}/{line_no}".format(
            po_id=po_id,
            line_no=line_no,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiSpendLimit]:
    if response.status_code == 200:
        response_200 = AiSpendLimit.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiSpendLimit]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiSpendLimitInput,
) -> Response[AiSpendLimit]:
    """[Buyer] Sets an approved order line's amount as its invoicer's spending ceiling for the month (AWS
    Budgets, an OpenAI project limit, an Anthropic workspace limit, a Google Cloud budget or spend cap,
    an Azure budget), reads it back and records the write. Refused below the month to date, with the
    figures. Raising the line raises it; closing the order removes it. An agent's call is a request the
    person confirms. 'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):
        body (SetAiSpendLimitInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendLimit]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        line_no=line_no,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiSpendLimitInput,
) -> Optional[AiSpendLimit]:
    """[Buyer] Sets an approved order line's amount as its invoicer's spending ceiling for the month (AWS
    Budgets, an OpenAI project limit, an Anthropic workspace limit, a Google Cloud budget or spend cap,
    an Azure budget), reads it back and records the write. Refused below the month to date, with the
    figures. Raising the line raises it; closing the order removes it. An agent's call is a request the
    person confirms. 'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):
        body (SetAiSpendLimitInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiSpendLimit
    """

    return sync_detailed(
        po_id=po_id,
        line_no=line_no,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiSpendLimitInput,
) -> Response[AiSpendLimit]:
    """[Buyer] Sets an approved order line's amount as its invoicer's spending ceiling for the month (AWS
    Budgets, an OpenAI project limit, an Anthropic workspace limit, a Google Cloud budget or spend cap,
    an Azure budget), reads it back and records the write. Refused below the month to date, with the
    figures. Raising the line raises it; closing the order removes it. An agent's call is a request the
    person confirms. 'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):
        body (SetAiSpendLimitInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendLimit]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        line_no=line_no,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiSpendLimitInput,
) -> Optional[AiSpendLimit]:
    """[Buyer] Sets an approved order line's amount as its invoicer's spending ceiling for the month (AWS
    Budgets, an OpenAI project limit, an Anthropic workspace limit, a Google Cloud budget or spend cap,
    an Azure budget), reads it back and records the write. Refused below the month to date, with the
    figures. Raising the line raises it; closing the order removes it. An agent's call is a request the
    person confirms. 'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):
        body (SetAiSpendLimitInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiSpendLimit
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            line_no=line_no,
            client=client,
            body=body,
        )
    ).parsed
