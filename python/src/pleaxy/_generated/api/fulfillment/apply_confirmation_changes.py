from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_confirmation_changes_result import ApplyConfirmationChangesResult
from ...types import Response


def _get_kwargs(
    po_id: str,
    confirmation_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/purchase-orders/{po_id}/confirmations/{confirmation_id}/apply".format(
            po_id=po_id,
            confirmation_id=confirmation_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApplyConfirmationChangesResult]:
    if response.status_code == 201:
        response_201 = ApplyConfirmationChangesResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApplyConfirmationChangesResult]:
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
) -> Response[ApplyConfirmationChangesResult]:
    """[Buyer] Take the new quantities and unit prices in the supplier's latest confirmation (outcome
    changed) into the order: { purchaseOrder, confirmation }. An ordinary line edit, as
    UpdatePurchaseOrder: the order gets a new version, goes back to approval when its rules say so, and
    the supplier hears po_changed. 409 CONFIRMATION_SUPERSEDED when the supplier confirmed again since,
    CONFIRMATION_DECIDED when it was already applied or declined, NO_CHANGES, or ORDER_NOT_OPEN.

    Args:
        po_id (str):
        confirmation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyConfirmationChangesResult]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        confirmation_id=confirmation_id,
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
) -> Optional[ApplyConfirmationChangesResult]:
    """[Buyer] Take the new quantities and unit prices in the supplier's latest confirmation (outcome
    changed) into the order: { purchaseOrder, confirmation }. An ordinary line edit, as
    UpdatePurchaseOrder: the order gets a new version, goes back to approval when its rules say so, and
    the supplier hears po_changed. 409 CONFIRMATION_SUPERSEDED when the supplier confirmed again since,
    CONFIRMATION_DECIDED when it was already applied or declined, NO_CHANGES, or ORDER_NOT_OPEN.

    Args:
        po_id (str):
        confirmation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyConfirmationChangesResult
    """

    return sync_detailed(
        po_id=po_id,
        confirmation_id=confirmation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApplyConfirmationChangesResult]:
    """[Buyer] Take the new quantities and unit prices in the supplier's latest confirmation (outcome
    changed) into the order: { purchaseOrder, confirmation }. An ordinary line edit, as
    UpdatePurchaseOrder: the order gets a new version, goes back to approval when its rules say so, and
    the supplier hears po_changed. 409 CONFIRMATION_SUPERSEDED when the supplier confirmed again since,
    CONFIRMATION_DECIDED when it was already applied or declined, NO_CHANGES, or ORDER_NOT_OPEN.

    Args:
        po_id (str):
        confirmation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyConfirmationChangesResult]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        confirmation_id=confirmation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    confirmation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApplyConfirmationChangesResult]:
    """[Buyer] Take the new quantities and unit prices in the supplier's latest confirmation (outcome
    changed) into the order: { purchaseOrder, confirmation }. An ordinary line edit, as
    UpdatePurchaseOrder: the order gets a new version, goes back to approval when its rules say so, and
    the supplier hears po_changed. 409 CONFIRMATION_SUPERSEDED when the supplier confirmed again since,
    CONFIRMATION_DECIDED when it was already applied or declined, NO_CHANGES, or ORDER_NOT_OPEN.

    Args:
        po_id (str):
        confirmation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyConfirmationChangesResult
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            confirmation_id=confirmation_id,
            client=client,
        )
    ).parsed
