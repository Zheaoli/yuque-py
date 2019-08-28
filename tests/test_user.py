from yuque_py.models.user import User


def test_user_get_with_login(mock_client):
    user = User(mock_client)
    user.get("abc")
    assert mock_client.api == f"users/abc"


def test_user_get_with_no_login(mock_client):
    user = User(mock_client)
    user.get()
    assert mock_client.api == f"user"
