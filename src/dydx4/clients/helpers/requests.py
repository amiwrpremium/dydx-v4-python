from typing import Optional, Any, Dict
import json

import requests

from ..errors import DydxApiError
from ..helpers.request_helpers import remove_nones

# TODO: Use a separate session per client instance.
session = requests.session()
session.headers.update(
    {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "dydx/python",
    }
)


class Response(object):
    def __init__(
        self,
        status_code: int,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ):
        if data is None:
            data = {}
        self.status_code = status_code
        self.data = data
        self.headers = headers


def request(
    uri: str,
    method: str,
    headers: Optional[Dict[str, Any]] = None,
    data_values: Optional[Dict[str, Any]] = None,
    api_timeout: Optional[int] = None,
) -> Response:
    if headers is None:
        headers = {}
    if data_values is None:
        data_values = {}
    response = send_request(
        uri,
        method,
        headers,
        data=json.dumps(remove_nones(data_values)),
        timeout=api_timeout,
    )
    if not str(response.status_code).startswith("2"):
        raise DydxApiError(response)

    if response.content:
        return Response(response.status_code, response.json(), response.headers)
    else:
        return Response(response.status_code, {}, response.headers)


def send_request(uri, method, headers=None, **kwargs):
    return getattr(session, method)(uri, headers=headers, **kwargs)
