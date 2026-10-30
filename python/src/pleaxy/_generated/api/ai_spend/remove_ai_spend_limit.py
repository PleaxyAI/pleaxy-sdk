from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_spend_limit import AiSpendLimit
from ...types import Response


def _get_kwargs(
    po_id: str,
    line_no: float,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/ai-spend/limits/{po_id}/{line_no}".format(
            po_id=po_id,
            line_no=line_no,
        ),
    }

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
) -> Response[AiSpendLimit]:
    """[Buyer] Removes the ceiling Pleaxy set for an order line (only one Pleaxy named) and records it.
    'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendLimit]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        line_no=line_no,
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
) -> Optional[AiSpendLimit]:
    """[Buyer] Removes the ceiling Pleaxy set for an order line (only one Pleaxy named) and records it.
    'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):

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
    ).parsed


async def asyncio_detailed(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AiSpendLimit]:
    """[Buyer] Removes the ceiling Pleaxy set for an order line (only one Pleaxy named) and records it.
    'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiSpendLimit]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        line_no=line_no,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    line_no: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AiSpendLimit]:
    """[Buyer] Removes the ceiling Pleaxy set for an order line (only one Pleaxy named) and records it.
    'edit' on purchase orders.

    Args:
        po_id (str):
        line_no (float):

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
        )
    ).parsed
