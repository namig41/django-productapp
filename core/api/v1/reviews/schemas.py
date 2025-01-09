from datetime import datetime

from pydantic import BaseModel


class ReviewInSchema(BaseModel):
    rating: int
    text: str


class CreateReviewSchema(BaseModel):
    product_id: int
    customer_token: str
    review: ReviewInSchema


class CreateReviewOutSchema(ReviewInSchema):
    id: int
    created_at: datetime | None
    updated_at: datetime | None
