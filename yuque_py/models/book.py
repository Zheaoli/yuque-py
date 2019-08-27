import datetime

from .user import User


class BookSerializer:
    _id: int
    _type: str
    _slug: str
    _name: str
    _namespace: str
    _user_id: int
    _user: User
    _description: str
    _creator_id: int
    _public: int
    _likes_count: int
    _watches_count: int
    _created_at: datetime.datetime
    _updated_at: datetime.datetime

    def __init__(self, **kwargs) -> None:
        self._id = kwargs.get("id")
        self._type = kwargs.get("type")
        self._slug = kwargs.get("slug")
        self._name = kwargs.get("name")
        self._namespace = kwargs.get("namespace")
        self._user_id = kwargs.get("user_id")
        self._user = User(**kwargs.get("user"))
        self._description = kwargs.get("description")
        self._creator_id = kwargs.get("creator_id")
        self._public = kwargs.get("public")
        self._likes_count = kwargs.get("likes_count")
        self._watches_count = kwargs.get("watches_count")
        self._created_at = kwargs.get("created_at")
        self._updated_at = kwargs.get("updated_at")

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def slug(self) -> str:
        return self.slug

    @property
    def name(self) -> str:
        return self._name

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def user(self) -> User:
        return self._user

    @property
    def description(self) -> str:
        return self._description

    @property
    def creator_id(self) -> int:
        return self._creator_id

    @property
    def public(self) -> int:
        return self._public

    @property
    def likes_count(self) -> int:
        return self._likes_count

    @property
    def watches_count(self) -> int:
        return self._watches_count

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self._updated_at
