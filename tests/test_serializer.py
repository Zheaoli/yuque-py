from yuque_py.models.serializers import UserSerializer
from yuque_py.models.user import User


def test_user_serializer():
    test_data = """
   {
    "id": 6,
    "type": "User",
    "login": "huacnlee",
    "name": "李华顺",
    "description": null,
    "avatar_url": "https://...png",
    "created_at": "2016-08-19T01:37:44.000Z",
    "updated_at": "2016-09-08T18:55:52.000Z"
  }
   """
    temp_data = UserSerializer(unknown=True).loads(test_data)
    user = User(**temp_data)
    assert user.id == 6


