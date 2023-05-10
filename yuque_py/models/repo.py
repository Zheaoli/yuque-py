import typing
import warnings
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
    
    def list_toc(self, namespace: str) -> typing.Dict:
        warnings.warn("Toc api will be updated in the future, please refer to https://www.yuque.com/yuque/developer/ag3xgd for more information", DeprecationWarning)
        assert namespace
        return self._client.request(f"repos/{namespace}/toc", method="GET")
    
    def update_toc(self, namespace: str, data: typing.Dict) -> typing.Dict:
        warnings.warn("Toc api will be updated in the future, please refer to https://www.yuque.com/yuque/developer/ag3xgd for more information", DeprecationWarning)
        assert namespace
        assert data
        return self._client.request(f"repos/{namespace}/toc",method="PUT",requests_data=data)


    @staticmethod
    def _get_url(user: typing.Optional[str], group: typing.Optional[str]):
        assert user or group
        api = f"users/{user}/repos" if user else f"groups/{group}/repos"
        return api
