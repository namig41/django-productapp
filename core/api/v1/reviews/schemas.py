from datetime import datetime

from pydantic import BaseModel

from core.app.products.entities.reviews import Review as ReviewEntity


class ReviewInSchema(BaseModel):
    text: str
    rating: int

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            text=self.text,
            rating=self.rating,
        )


class CreateReviewSchema(BaseModel):
    product_id: int
    customer_token: str
    review: ReviewInSchema


class ReviewOutSchema(ReviewInSchema):
    id: int
    created_at: datetime | None
    updated_at: datetime | None

    @classmethod
    def from_entity(cls, review: ReviewEntity) -> "ReviewOutSchema":
        return cls(
            id=review.id,
            text=review.text,
            rating=review.rating,
            created_at=review.created_at,
            updated_at=review.updated_at,
        )
