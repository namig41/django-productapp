from abc import (
    ABC,
    abstractmethod,
)

from core.app.customers.entities import Customer


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, customer: Customer, code: str) -> None: ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: Customer, code: str) -> None:
        print(f"Code sent: {code}")
