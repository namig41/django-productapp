from dataclasses import (
    dataclass,
    field,
)

from apps.common.enums import EntityStatus
from apps.customers.models import Customer
from apps.products.entities.products import Product


@dataclass
class Review:
    customer: Customer | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default="")
    rating: int
