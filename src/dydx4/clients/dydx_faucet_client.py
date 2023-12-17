from typing import Optional, Dict, Any
from .helpers.request_helpers import generate_query_path
from .helpers.requests import request, Response
from .constants import DEFAULT_API_TIMEOUT


class FaucetClient(object):
    def __init__(
        self,
        host: str,
        api_timeout: Optional[int] = None,
    ):
        self.host = host
        self.api_timeout = api_timeout or DEFAULT_API_TIMEOUT

    # ============ Request Helpers ============

    # def _post(self, request_path, params={}, body={}) -> Response:
    def _post(
        self,
        request_path: str,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ) -> Response:
        if params is None:
            params = {}
        if body is None:
            body = {}
        return request(
            generate_query_path(self.host + request_path, params),
            "post",
            data_values=body,
            api_timeout=self.api_timeout,
        )

    # ============ Requests ============

    def fill(
        self,
        address: str,
        subaccount_number: int,
        amount: int,
    ) -> Response:
        """
        fill account

        :param address: required
        :type address: str

        :param subaccount_number: required
        :type subaccount_number: int

        :param amount: required
        :type amount: int

        :returns:

        :raises: DydxAPIError
        """
        path = "/faucet/tokens"
        return self._post(
            path,
            {},
            {
                "address": address,
                "subaccountNumber": subaccount_number,
                "amount": amount,
            },
        )

    def fill_native(
        self,
        address: str,
    ) -> Response:
        """
        fill account with native token

        :param address: required
        :type address: str

        :returns:

        :raises: DydxAPIError
        """
        path = "/faucet/native-token"
        return self._post(
            path,
            {},
            {
                "address": address,
            },
        )
