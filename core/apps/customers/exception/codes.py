from dataclasses import dataclass

from core.apps.common.exception import ServiceException


@dataclass(eq=False)
class CodeException(ServiceException):
    @property
    def message(self) -> str:
        return "Auth code occurred"


@dataclass(eq=False)
class CodeNotFoundException(ServiceException):
    code: str

    @property
    def message(self) -> str:
        return "Code not found"


@dataclass(eq=False)
class CodeNotEqualException(CodeException):
    code: str
    cached_code: str
    customer_phone: str

    @property
    def message(self) -> str:
        return "Codes are not equal"
