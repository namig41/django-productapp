from dataclasses import dataclass

from core.app.common.exceptions import ServiceException


@dataclass(eq=False)
class CustomerTokenInvalid(ServiceException):
    token: str

    @property
    def message(self) -> str:
        return "A customer with provided is not found"
