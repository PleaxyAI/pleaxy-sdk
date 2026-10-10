from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_chain_settings import ApprovalChainSettings
from ...models.update_approval_chain_input import UpdateApprovalChainInput
from ...types import Response


def _get_kwargs(
    process: str,
    *,
    body: UpdateApprovalChainInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/approval-chains/{process}".format(
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
) -> Optional[ApprovalChainSettings]:
    if response.status_code == 200:
        response_200 = ApprovalChainSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApprovalChainSettings]:
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
    body: UpdateApprovalChainInput,
) -> Response[ApprovalChainSettings]:
    """[Buyer] Configure the approval chain for a process - its stages, a link to another process's chain,
    or `useDefault: true` for the region-administrator default. Needs a signed-in session.

    Args:
        process (str):
        body (UpdateApprovalChainInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalChainSettings]
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
    body: UpdateApprovalChainInput,
) -> Optional[ApprovalChainSettings]:
    """[Buyer] Configure the approval chain for a process - its stages, a link to another process's chain,
    or `useDefault: true` for the region-administrator default. Needs a signed-in session.

    Args:
        process (str):
        body (UpdateApprovalChainInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalChainSettings
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
    body: UpdateApprovalChainInput,
) -> Response[ApprovalChainSettings]:
    """[Buyer] Configure the approval chain for a process - its stages, a link to another process's chain,
    or `useDefault: true` for the region-administrator default. Needs a signed-in session.

    Args:
        process (str):
        body (UpdateApprovalChainInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalChainSettings]
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
    body: UpdateApprovalChainInput,
) -> Optional[ApprovalChainSettings]:
    """[Buyer] Configure the approval chain for a process - its stages, a link to another process's chain,
    or `useDefault: true` for the region-administrator default. Needs a signed-in session.

    Args:
        process (str):
        body (UpdateApprovalChainInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalChainSettings
    """

    return (
        await asyncio_detailed(
            process=process,
            client=client,
            body=body,
        )
    ).parsed
