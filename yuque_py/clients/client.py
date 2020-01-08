import typing

import requests
from urllib.parse import urlencode

from .abstract_client import AbstractClient
from yuque_py.exceptions.request_error import RequestError


class Client(AbstractClient):
    api_host: str
    user_token: str

    def __init__(self, api_host: str, user_token: str) -> None:
        self.api_host = api_host
        self.user_token = user_token

    def request(
        self,
        api: str,
        method: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]] = None,
        user_agent: str = "@yuque/sdk",
    ) -> typing.Dict:
        request_url = f"{self.api_host}/{api}"
        request_header = {"User-Agent": user_agent, "X-Auth-Token": self.user_token}
        if method == "GET":
            func = self._get_request
        elif method == "POST":
            request_header["Content-Type"] = "application/json"
            func = self._post_request
        elif method == "PUT":
            request_header["Content-Type"] = "application/json"
            func = self._put_request
        elif method == "DELETE":
            func = self._delete_request
        else:
            raise ValueError
        response = func(request_url, requests_data, request_header)
        if response.status_code != 200:
            raise RequestError(response.status_code, response.text)
        return response.json()

    @staticmethod
    def _get_request(
        request_url: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]],
        request_header: typing.Dict[str, str],
    ) -> requests.Response:
        if requests_data:
            request_url = f"{request_url}&{urlencode(requests_data)}"

        return requests.get(request_url, headers=request_header)

    @staticmethod
    def _post_request(
        request_url: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]],
        request_header: typing.Dict[str, str],
    ) -> requests.Response:
        return requests.post(request_url, json=requests_data, headers=request_header)

    @staticmethod
    def _put_request(
        request_url: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]],
        request_header: typing.Dict[str, str],
    ) -> requests.Response:
        return requests.put(request_url, json=requests_data, headers=request_header)

    @staticmethod
    def _delete_request(
        request_url: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]],
        request_header: typing.Dict[str, str],
    ) -> requests.Response:
        return requests.delete(request_url, headers=request_header)
