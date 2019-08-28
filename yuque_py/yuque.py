from yuque_py.models import User, Group, Repo, Doc
from yuque_py.clients.client import Client


class Yuque:
    def __init__(self, api_host: str, user_token: str):
        self._client = Client(api_host, user_token)
        self.users = User(self._client)
        self.groups = Group(self._client)
        self.repos = Repo(self._client)
        self.docs = Doc(self._client)
