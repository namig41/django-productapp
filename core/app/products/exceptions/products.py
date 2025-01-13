from dataclasses import dataclass

from core.app.common.exceptions import ServiceException


@dataclass(eq=False)
class ProductNotFound(ServiceException):
    product_id: int

    @property
    def message(self) -> str:
        return "A product with provided is not found"
