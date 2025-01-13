from abc import (
    ABC,
    abstractmethod,
)
from random import SystemRandom

from django.core.cache import cache

from core.app.customers.entities import Customer
from core.app.customers.exceptions.codes import (
    CodeNotEqualException,
    CodeNotFoundException,
)


class BaseCodeService(ABC):
    @abstractmethod
    def generate_code(self, customer: Customer) -> str: ...
    @abstractmethod
    def validate_code(self, code: str, customer: Customer) -> None: ...


class DjangoCacheCodeService(BaseCodeService):
    def generate_code(self, customer: Customer) -> str:
        code = str(SystemRandom().randint(100000, 999999))
        cache.set(customer.phone, code)

        return code

    def validate_code(self, code: str, customer: Customer) -> None:
        cached_code = cache.get(customer.phone)

        if cached_code is None:
            raise CodeNotFoundException(code=code)

        if cached_code != code:
            raise CodeNotEqualException(
                code=code,
                cached_code=cached_code,
                customer_phone=customer.phone,
            )
