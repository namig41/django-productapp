from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.app.common.enums import EntityStatus
from core.app.customers.models import Customer
from core.app.products.entities.products import Product


@dataclass
class Review:
    id: int | None = field(default=None, kw_only=True)
    customer: Customer | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)

    text: str = field(default="")
    rating: int = field(default=1)

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime | None = field(default=None)
