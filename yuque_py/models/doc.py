import typing

from yuque_py.clients.abstract_client import AbstractClient


class Doc:
    def __init__(self, client: AbstractClient):
        self._client = client

    def get(
        self, namespace: str, slug: str, data: typing.Optional[typing.Dict] = None
    ) -> typing.Dict:
        assert namespace
        assert slug
        api = f"repos/{namespace}/docs/{slug}"
        return self._client.request(api, method="GET", requests_data=data)

    def create(
        self, namespace: str, data: typing.Optional[typing.Dict] = None
    ) -> typing.Dict:
        assert namespace
        api = f"repos/{namespace}/docs"
        return self._client.request(api, method="POST", requests_data=data)

    def update(
        self, namespace: str, doc_id: str, data: typing.Optional[typing.Dict] = None
    ) -> typing.Dict:
        assert namespace
        assert doc_id
        api = f"repos/{namespace}/docs/{doc_id}"
        return self._client.request(api, method="PUT", requests_data=data)

    def delete(self, namespace: str, doc_id: str) -> typing.Dict:
        assert namespace
        assert doc_id
        api = f"repos/{namespace}/docs/{doc_id}"
        return self._client.request(api, method="DELETE")
