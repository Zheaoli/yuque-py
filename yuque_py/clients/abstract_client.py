import abc
import typing


class AbstractClient:
    @abc.abstractmethod
    def request(
        self,
        api: str,
        method: str,
        requests_data: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Dict:
        pass
