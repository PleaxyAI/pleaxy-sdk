from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_remittance_upload_input import RequestRemittanceUploadInput
from ...models.request_remittance_upload_result import RequestRemittanceUploadResult
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    body: RequestRemittanceUploadInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/remittance-upload".format(
            invoice_id=invoice_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequestRemittanceUploadResult]:
    if response.status_code == 200:
        response_200 = RequestRemittanceUploadResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequestRemittanceUploadResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestRemittanceUploadInput,
) -> Response[RequestRemittanceUploadResult]:
    """[Buyer] A presigned URL to upload a proof of payment (a bank's transfer receipt) for an approved or
    paid invoice: { contentType: application/pdf|image/png|image/jpeg }. PUT the file to uploadUrl with
    that Content-Type within 5 minutes, up to maxBytes (10 MB), then send its fileId with SendRemittance
    or RecordPayment's remittance. An upload nothing attaches is deleted after a couple of days. Human
    session only.

    Args:
        invoice_id (str):
        body (RequestRemittanceUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestRemittanceUploadResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestRemittanceUploadInput,
) -> Optional[RequestRemittanceUploadResult]:
    """[Buyer] A presigned URL to upload a proof of payment (a bank's transfer receipt) for an approved or
    paid invoice: { contentType: application/pdf|image/png|image/jpeg }. PUT the file to uploadUrl with
    that Content-Type within 5 minutes, up to maxBytes (10 MB), then send its fileId with SendRemittance
    or RecordPayment's remittance. An upload nothing attaches is deleted after a couple of days. Human
    session only.

    Args:
        invoice_id (str):
        body (RequestRemittanceUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestRemittanceUploadResult
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestRemittanceUploadInput,
) -> Response[RequestRemittanceUploadResult]:
    """[Buyer] A presigned URL to upload a proof of payment (a bank's transfer receipt) for an approved or
    paid invoice: { contentType: application/pdf|image/png|image/jpeg }. PUT the file to uploadUrl with
    that Content-Type within 5 minutes, up to maxBytes (10 MB), then send its fileId with SendRemittance
    or RecordPayment's remittance. An upload nothing attaches is deleted after a couple of days. Human
    session only.

    Args:
        invoice_id (str):
        body (RequestRemittanceUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequestRemittanceUploadResult]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RequestRemittanceUploadInput,
) -> Optional[RequestRemittanceUploadResult]:
    """[Buyer] A presigned URL to upload a proof of payment (a bank's transfer receipt) for an approved or
    paid invoice: { contentType: application/pdf|image/png|image/jpeg }. PUT the file to uploadUrl with
    that Content-Type within 5 minutes, up to maxBytes (10 MB), then send its fileId with SendRemittance
    or RecordPayment's remittance. An upload nothing attaches is deleted after a couple of days. Human
    session only.

    Args:
        invoice_id (str):
        body (RequestRemittanceUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequestRemittanceUploadResult
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
