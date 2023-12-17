from typing import Any
from requests import Response


class DydxError(Exception):
    """Base error class for all exceptions raised in this library.
    Will never be raised naked; more specific subclasses of this exception will
    be raised when appropriate."""


class ValueTooLargeError(DydxError):
    pass


class EmptyMsgError(DydxError):
    pass


class NotFoundError(DydxError):
    pass


class UndefinedError(DydxError):
    pass


class DecodeError(DydxError):
    pass


class ConvertError(DydxError):
    pass


class SchemaError(DydxError):
    pass


class DydxApiError(DydxError):
    def __init__(self, response: Response) -> None:
        self.status_code = response.status_code
        try:
            self.msg = response.json()
        except ValueError:
            self.msg = response.text
        self.response = response
        self.request = getattr(response, "request", None)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"DydxApiError(status_code={self.status_code}, response={self.msg})"


class TransactionReverted(DydxError):
    def __init__(self, tx_receipt: Any):
        self.tx_receipt = tx_receipt
