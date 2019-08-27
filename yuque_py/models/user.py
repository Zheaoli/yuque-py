import datetime


class User:
    _id: int
    _type: str
    _name: str
    _avatar_url: str
    _created_at: datetime.datetime
    _updated_at: datetime.datetime

    def __init__(self, **kwargs) -> None:
        self._id = kwargs.get("id")
        self._type = kwargs.get("type")
        self._login = kwargs.get("login")
        self._name = kwargs.get("name")
        self._avatar_url = kwargs.get("avatar_url")
        self._created_at = kwargs.get("created_at")
        self._updated_at = kwargs.get("updated_at")

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def login(self) -> str:
        return self._login

    @property
    def name(self) -> str:
        return self._name

    @property
    def avatar_url(self) -> str:
        return self.avatar_url

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self._updated_at




