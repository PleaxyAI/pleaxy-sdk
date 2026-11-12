from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_credit_note_view import BuyerCreditNoteView
from ...types import Response


def _get_kwargs(
    credit_note_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/credit-notes/{credit_note_id}/accept".format(
            credit_note_id=credit_note_id,
        ),
    }

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
) -> Response[BuyerCreditNoteView]:
    """[Buyer] Accept a credit note. A correction gives PO balance back; when Pleaxy settles credits, it's
    applied to the unpaid invoice it corrects.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerCreditNoteView]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BuyerCreditNoteView]:
    """[Buyer] Accept a credit note. A correction gives PO balance back; when Pleaxy settles credits, it's
    applied to the unpaid invoice it corrects.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuyerCreditNoteView
    """

    return sync_detailed(
        credit_note_id=credit_note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[BuyerCreditNoteView]:
    """[Buyer] Accept a credit note. A correction gives PO balance back; when Pleaxy settles credits, it's
    applied to the unpaid invoice it corrects.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuyerCreditNoteView]
    """

    kwargs = _get_kwargs(
        credit_note_id=credit_note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[BuyerCreditNoteView]:
    """[Buyer] Accept a credit note. A correction gives PO balance back; when Pleaxy settles credits, it's
    applied to the unpaid invoice it corrects.

    Args:
        credit_note_id (str):

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
        )
    ).parsed
