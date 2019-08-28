import typing

from yuque_py.clients.abstract_client import AbstractClient


class Group:
    def __init__(self, client: AbstractClient):
        self._client = client

    def list(
        self,
        login: typing.Optional[str] = None,
        data: typing.Optional[typing.Dict] = None,
    ) -> typing.Dict:
        api = f"users/{login}/groups" if login else "groups"
        return self._client.request(api, method="GET", requests_data=data)

    def create(self, data: typing.Dict) -> typing.Dict:
        assert "name" in data
        assert "login" in data
        api = "groups"
        return self._client.request(api, method="POST", requests_data=data)

    def get(self, login: str) -> typing.Dict:
        assert login
        api = f"groups/{login}"
        return self._client.request(api, method="GET")

    def update(self, login: str, data: typing.Dict) -> typing.Dict:
        assert login
        api = f"groups/{login}"
        return self._client.request(api, method="PUT", requests_data=data)

    def delete(self, login: str) -> typing.Dict:
        assert login
        api = f"groups/{login}"
        return self._client.request(api, method="DELETE")

    def list_user(self, login: str) -> typing.Dict:
        return self._client.request(f"groups/{login}/users", method="GET")

    def add_user(self, group: str, user: str, data: typing.Dict) -> typing.Dict:
        assert group
        assert user
        api = f"groups/{group}/users/{user}"
        return self._client.request(api, method="PUT", requests_data=data)

    def remove_user(self, group: str, user: str) -> typing.Dict:
        assert group
        assert user
        api = f"groups/{group}/users/{user}"
        return self._client.request(api, method="DELETE")

    @staticmethod
    def _get_url(user: str, group: str):
        assert user or group
        api = f"users/{user}/repos" if user else f"users/{group}/repos"
        return api
