import pytest

from yuque_py.models.group import Group


def test_group_list_with_user(mock_client):
    group = Group(mock_client)
    group.list("bac")
    assert mock_client.api == "users/bac/groups"


def test_group_list_without_user(mock_client):
    group = Group(mock_client)
    group.list()
    assert mock_client.api == "groups"


def test_group_create(mock_client):
    group = Group(mock_client)
    data = {
        "name": 1,
        "login": "abc"
    }
    group.create(data)
    assert mock_client.request_data == data


def test_group_create_with_assert_error(mock_client):
    group = Group(mock_client)
    data = {
        "login": "abc"
    }
    with pytest.raises(AssertionError):
        group.create(data)


def test_group_get(mock_client):
    group = Group(mock_client)
    group.get("abc")
    assert mock_client.api == "groups/abc"


def test_group_update(mock_client):
    group = Group(mock_client)
    group.update("abc", {})
    assert mock_client.api == "groups/abc"


def test_group_delete(mock_client):
    group = Group(mock_client)
    group.delete("abc")
    assert mock_client.api == "groups/abc"


def test_group_list_user(mock_client):
    group = Group(mock_client)
    group.list_user("abc")
    assert mock_client.api == "groups/abc/users"
