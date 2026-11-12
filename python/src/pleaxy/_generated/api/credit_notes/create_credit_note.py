from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_credit_note_view import BuyerCreditNoteView
from ...models.create_credit_note_input import CreateCreditNoteInput
from ...models.supplier_credit_note_view import SupplierCreditNoteView
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCreditNoteInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/credit-notes",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union["BuyerCreditNoteView", "SupplierCreditNoteView"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_create_credit_note_result_type_0 = (
                    SupplierCreditNoteView.from_dict(data)
                )

                return componentsschemas_create_credit_note_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_create_credit_note_result_type_1 = (
                BuyerCreditNoteView.from_dict(data)
            )

            return componentsschemas_create_credit_note_result_type_1

        response_201 = _parse_response_201(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCreditNoteInput,
) -> Response[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] Issue a credit note against the invoice it corrects (invoiceId) or a counterparty
    (connectionId); a buyer records one it received the same way, optionally from a document Pleaxy read
    (sourceImportId). Its total is computed from its lines and tax. One that corrects an invoice and
    isn't for more than it is accepted at once; otherwise the buyer accepts or rejects it.

    Args:
        body (CreateCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BuyerCreditNoteView', 'SupplierCreditNoteView']]
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
    body: CreateCreditNoteInput,
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] Issue a credit note against the invoice it corrects (invoiceId) or a counterparty
    (connectionId); a buyer records one it received the same way, optionally from a document Pleaxy read
    (sourceImportId). Its total is computed from its lines and tax. One that corrects an invoice and
    isn't for more than it is accepted at once; otherwise the buyer accepts or rejects it.

    Args:
        body (CreateCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BuyerCreditNoteView', 'SupplierCreditNoteView']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCreditNoteInput,
) -> Response[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] Issue a credit note against the invoice it corrects (invoiceId) or a counterparty
    (connectionId); a buyer records one it received the same way, optionally from a document Pleaxy read
    (sourceImportId). Its total is computed from its lines and tax. One that corrects an invoice and
    isn't for more than it is accepted at once; otherwise the buyer accepts or rejects it.

    Args:
        body (CreateCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BuyerCreditNoteView', 'SupplierCreditNoteView']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCreditNoteInput,
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] Issue a credit note against the invoice it corrects (invoiceId) or a counterparty
    (connectionId); a buyer records one it received the same way, optionally from a document Pleaxy read
    (sourceImportId). Its total is computed from its lines and tax. One that corrects an invoice and
    isn't for more than it is accepted at once; otherwise the buyer accepts or rejects it.

    Args:
        body (CreateCreditNoteInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BuyerCreditNoteView', 'SupplierCreditNoteView']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
