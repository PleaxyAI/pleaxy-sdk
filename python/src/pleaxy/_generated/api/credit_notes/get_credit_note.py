from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.buyer_credit_note_view import BuyerCreditNoteView
from ...models.supplier_credit_note_view import SupplierCreditNoteView
from ...types import Response


def _get_kwargs(
    credit_note_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/credit-notes/{credit_note_id}".format(
            credit_note_id=credit_note_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["BuyerCreditNoteView", "SupplierCreditNoteView"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_get_credit_note_result_type_0 = (
                    SupplierCreditNoteView.from_dict(data)
                )

                return componentsschemas_get_credit_note_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_get_credit_note_result_type_1 = (
                BuyerCreditNoteView.from_dict(data)
            )

            return componentsschemas_get_credit_note_result_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
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
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] One credit note, with what it corrects, the PO balance it gave back, where its money went and
    what's left of it.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BuyerCreditNoteView', 'SupplierCreditNoteView']]
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
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] One credit note, with what it corrects, the PO balance it gave back, where its money went and
    what's left of it.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BuyerCreditNoteView', 'SupplierCreditNoteView']
    """

    return sync_detailed(
        credit_note_id=credit_note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    credit_note_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] One credit note, with what it corrects, the PO balance it gave back, where its money went and
    what's left of it.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['BuyerCreditNoteView', 'SupplierCreditNoteView']]
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
) -> Optional[Union["BuyerCreditNoteView", "SupplierCreditNoteView"]]:
    """[Both] One credit note, with what it corrects, the PO balance it gave back, where its money went and
    what's left of it.

    Args:
        credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['BuyerCreditNoteView', 'SupplierCreditNoteView']
    """

    return (
        await asyncio_detailed(
            credit_note_id=credit_note_id,
            client=client,
        )
    ).parsed
