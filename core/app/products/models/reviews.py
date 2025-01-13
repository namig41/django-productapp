from django.db import models

from core.app.common.models import TimedBaseModel
from core.app.customers.entities import Customer as CustomerEntity
from core.app.products.entities.products import Product as ProductEntity
from core.app.products.entities.reviews import Review as ReviewEntity


class Review(TimedBaseModel):
    customer = models.ForeignKey(
        to="customers.Customer",
        verbose_name="Reviewer",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to="products.Product",
        verbose_name="Product",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="User rating",
        default=1,
    )
    text = models.TextField(verbose_name="Review text", blank=True, default="")

    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        customer: CustomerEntity,
        product: ProductEntity,
    ) -> "Review":
        return cls(
            pk=review.id,
            product_id=product.id,
            cusomter_id=customer.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(
        self,
    ) -> ReviewEntity:
        return ReviewEntity(
            text=self.rating,
            rating=self.rating,
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Отзывы продуктов"
        verbose_name_plural = "Отзывы продуктов"
        unique_together = (("customer", "product"),)
