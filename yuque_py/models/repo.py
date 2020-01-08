import typing

from yuque_py.clients.abstract_client import AbstractClient


class Repo:
    def __init__(self, client: AbstractClient):
        self._client = client

    def list(
        self,
        user: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict] = None,
    ) -> typing.Dict:
        api = self._get_url(user, group)
        return self._client.request(api, method="GET", requests_data=data)

    def create(
        self,
        user: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict] = None,
    ) -> typing.Dict:
        api = self._get_url(user, group)
        assert data
        return self._client.request(api, method="POST", requests_data=data)

    def get(self, namespace: str, data: typing.Dict = None) -> typing.Dict:
        assert namespace
        return self._client.request(
            f"repos/{namespace}", method="GET", requests_data=data
        )

    def update(self, namespace: str, data: typing.Dict) -> typing.Dict:
        assert namespace
        return self._client.request(
            f"repos/{namespace}", method="PUT", requests_data=data
        )

    def delete(self, namespace: str) -> typing.Dict:
        assert namespace
        return self._client.request(f"repos/{namespace}", method="DELETE")

    @staticmethod
    def _get_url(user: typing.Optional[str], group: typing.Optional[str]):
        assert user or group
        api = f"users/{user}/repos" if user else f"groups/{group}/repos"
        return api
