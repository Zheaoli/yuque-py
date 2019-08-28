import typing

from yuque_py.clients.abstract_client import AbstractClient


class User:
    def __init__(self, client: AbstractClient):
        self._client = client

    def get(self, login: typing.Optional[str] = None) -> typing.Dict:
        api = f"users/{login}" if login else "user"
        return self._client.request(api=api, method="GET", requests_data=None)
