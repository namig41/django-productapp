from datetime import datetime

from pydantic import BaseModel

from core.app.products.entities.products import Product as ProductEntity


class ProductSchema(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: ProductEntity) -> "ProductSchema":
        return ProductSchema(
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


ProductListSchema = list[ProductSchema]
