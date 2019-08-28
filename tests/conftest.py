import typing

import pytest
from yuque_py.clients.client import Client
from yuque_py.clients.abstract_client import AbstractClient

API_HOST = "http://mock"
USER_TOKEN = "ABC"


@pytest.fixture
def standard_client():
    return Client(f"{API_HOST}", f"{USER_TOKEN}")


@pytest.fixture
def api_host():
    return API_HOST


@pytest.fixture
def user_token():
    return USER_TOKEN


class MockClient(AbstractClient):
    def __init__(self):
        self.api = None
        self.method = None
        self.request_data = None

    def request(
        self,
        api: str,
        method: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Dict:
        self.api = api
        self.method = method
        self.request_data = requests_data
        return {}


@pytest.fixture
def mock_client():
    return MockClient()
