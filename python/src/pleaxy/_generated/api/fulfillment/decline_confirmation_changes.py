from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.decline_confirmation_changes_input import DeclineConfirmationChangesInput
from ...models.order_confirmation import OrderConfirmation
from ...types import Response


def _get_kwargs(
    po_id: str,
    confirmation_id: str,
    *,
    body: DeclineConfirmationChangesInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/confirmations/{confirmation_id}/decline".format(
            po_id=po_id,
            confirmation_id=confirmation_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OrderConfirmation]:
    if response.status_code == 200:
        response_200 = OrderConfirmation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrderConfirmation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeclineConfirmationChangesInput,
) -> Response[OrderConfirmation]:
    """[Buyer] Keep the order as it is instead of the supplier's new quantities and prices: { reason? }
    (500 characters, shown to the supplier). Answers the confirmation with its decision; the supplier is
    told (po_changes_declined). The same 409s as ApplyConfirmationChanges.

    Args:
        po_id (str):
        confirmation_id (str):
        body (DeclineConfirmationChangesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderConfirmation]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        confirmation_id=confirmation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeclineConfirmationChangesInput,
) -> Optional[OrderConfirmation]:
    """[Buyer] Keep the order as it is instead of the supplier's new quantities and prices: { reason? }
    (500 characters, shown to the supplier). Answers the confirmation with its decision; the supplier is
    told (po_changes_declined). The same 409s as ApplyConfirmationChanges.

    Args:
        po_id (str):
        confirmation_id (str):
        body (DeclineConfirmationChangesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderConfirmation
    """

    return sync_detailed(
        po_id=po_id,
        confirmation_id=confirmation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeclineConfirmationChangesInput,
) -> Response[OrderConfirmation]:
    """[Buyer] Keep the order as it is instead of the supplier's new quantities and prices: { reason? }
    (500 characters, shown to the supplier). Answers the confirmation with its decision; the supplier is
    told (po_changes_declined). The same 409s as ApplyConfirmationChanges.

    Args:
        po_id (str):
        confirmation_id (str):
        body (DeclineConfirmationChangesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderConfirmation]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        confirmation_id=confirmation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeclineConfirmationChangesInput,
) -> Optional[OrderConfirmation]:
    """[Buyer] Keep the order as it is instead of the supplier's new quantities and prices: { reason? }
    (500 characters, shown to the supplier). Answers the confirmation with its decision; the supplier is
    told (po_changes_declined). The same 409s as ApplyConfirmationChanges.

    Args:
        po_id (str):
        confirmation_id (str):
        body (DeclineConfirmationChangesInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderConfirmation
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            confirmation_id=confirmation_id,
            client=client,
            body=body,
        )
    ).parsed
