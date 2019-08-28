import pytest

from yuque_py.models.repo import Repo


def test_repo_list_with_user(mock_client):
    repo = Repo(mock_client)
    repo.list("bac")
    assert mock_client.api == "users/bac/repos"


def test_repo_list_with_group(mock_client):
    repo = Repo(mock_client)
    repo.list(group="bac")
    assert mock_client.api == "groups/bac/repos"


def test_repo_list_with_assert_error(mock_client):
    repo = Repo(mock_client)
    with pytest.raises(AssertionError):
        repo.list()


def test_repo_create_with_user(mock_client):
    repo = Repo(mock_client)
    repo.list("bac")
    assert mock_client.api == "users/bac/repos"


def test_repo_create_with_group(mock_client):
    repo = Repo(mock_client)
    repo.list(group="bac")
    assert mock_client.api == "groups/bac/repos"


def test_repo_create_with_assert_error(mock_client):
    repo = Repo(mock_client)
    with pytest.raises(AssertionError):
        repo.list()


def test_repo_get(mock_client):
    repo = Repo(mock_client)
    repo.get("abc")
    assert mock_client.api == "repos/abc"


def test_repo_update(mock_client):
    repo = Repo(mock_client)
    repo.update("abc", {})
    assert mock_client.api == "repos/abc"


def test_delete_update(mock_client):
    repo = Repo(mock_client)
    repo.delete("abc")
    assert mock_client.api == "repos/abc"
