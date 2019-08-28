import json

import requests_mock
import pytest
from yuque_py.exceptions.request_error import RequestError


def test_get_request_with_no_data(standard_client, api_host, user_token):
    api = "abc"
    with requests_mock.Mocker() as m:
        request = m.get(f"{api_host}/{api}", json={"data": {}})
        response = standard_client.request(api, method="GET")
        assert request.last_request.path == f"/{api}"
        assert response == {"data": {}}
        assert request.last_request.headers["User-Agent"] == "@yuque/sdk"
        assert request.last_request.headers["X-Auth-Token"] == user_token


def test_get_request_with_query(standard_client, api_host, user_token):
    api = "abc"
    data = {"abc": 1}
    with requests_mock.Mocker() as m:
        request = m.get(f"{api_host}/{api}&abc=1", json={"data": {}})
        response = standard_client.request(api, method="GET", requests_data=data)
        assert request.last_request.path == f"/{api}&abc=1"
        assert response == {"data": {}}
        assert request.last_request.headers["User-Agent"] == "@yuque/sdk"
        assert request.last_request.headers["X-Auth-Token"] == user_token


def test_post_request(standard_client, api_host, user_token):
    api = "abc"
    data = {"abc": 1}
    with requests_mock.Mocker() as m:
        request = m.post(f"{api_host}/{api}", json={"data": {}})
        response = standard_client.request(api, method="POST", requests_data=data)
        assert json.loads(request.last_request.text) == data
        assert response == {"data": {}}
        assert request.last_request.headers["User-Agent"] == "@yuque/sdk"
        assert request.last_request.headers["X-Auth-Token"] == user_token
        assert request.last_request.headers["Content-Type"] == "application/json"


def test_put_request(standard_client, api_host, user_token):
    api = "abc"
    data = {"abc": 1}
    with requests_mock.Mocker() as m:
        request = m.put(f"{api_host}/{api}", json={"data": {}})
        response = standard_client.request(api, method="PUT", requests_data=data)
        assert json.loads(request.last_request.text) == data
        assert response == {"data": {}}
        assert request.last_request.headers["User-Agent"] == "@yuque/sdk"
        assert request.last_request.headers["X-Auth-Token"] == user_token
        assert request.last_request.headers["Content-Type"] == "application/json"


def test_delete_request(standard_client, api_host, user_token):
    api = "abc"
    with requests_mock.Mocker() as m:
        request = m.delete(f"{api_host}/{api}", json={"data": {}})
        response = standard_client.request(api, method="DELETE")
        assert response == {"data": {}}
        assert request.last_request.headers["User-Agent"] == "@yuque/sdk"
        assert request.last_request.headers["X-Auth-Token"] == user_token


def test_request_with_exception(standard_client, api_host, user_token):
    with pytest.raises(RequestError):
        api = "abc"
        with requests_mock.Mocker() as m:
            request = m.delete(f"{api_host}/{api}", status_code=401)
            response = standard_client.request(api, method="DELETE")
