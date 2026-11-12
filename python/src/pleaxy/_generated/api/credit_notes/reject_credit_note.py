from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_credit_note_view import BuyerCreditNoteView
from ...models.reject_credit_note_input import RejectCreditNoteInput
from ...types import Response


def _get_kwargs(
    credit_note_id: str,
    *,
    body: RejectCreditNoteInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/credit-notes/{credit_note_id}/reject".format(
            credit_note_id=credit_note_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BuyerCreditNoteView]:
    if response.status_code == 201:
        response_201 = BuyerCreditNoteView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BuyerCreditNoteView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RejectCreditNoteInput,
) -> Response[BuyerCreditNoteView]:
    """[Buyer] Reject a credit note waiting for acceptance, with a reason the supplier reads.

    Args:
        credit_note_id (str):
        body (RejectCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerCreditNoteView]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RejectCreditNoteInput,
) -> Optional[BuyerCreditNoteView]:
    """[Buyer] Reject a credit note waiting for acceptance, with a reason the supplier reads.

    Args:
        credit_note_id (str):
        body (RejectCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyerCreditNoteView
    """

    return sync_detailed(
        credit_note_id=credit_note_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RejectCreditNoteInput,
) -> Response[BuyerCreditNoteView]:
    """[Buyer] Reject a credit note waiting for acceptance, with a reason the supplier reads.

    Args:
        credit_note_id (str):
        body (RejectCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerCreditNoteView]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RejectCreditNoteInput,
) -> Optional[BuyerCreditNoteView]:
    """[Buyer] Reject a credit note waiting for acceptance, with a reason the supplier reads.

    Args:
        credit_note_id (str):
        body (RejectCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyerCreditNoteView
    """

    return (
        await asyncio_detailed(
            credit_note_id=credit_note_id,
            client=client,
            body=body,
        )
    ).parsed
