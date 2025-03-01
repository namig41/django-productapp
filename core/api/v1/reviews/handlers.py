from django.http import HttpResponse
from ninja import (
    Header,
    Router,
)
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    ReviewInSchema,
    ReviewOutSchema,
)
from core.app.common.exceptions import ServiceException
from core.app.products.entities.reviews import Review as ReviewEntity
from core.app.products.use_cases.reviews.create import CreateReviewUseCase
from core.project.containers import get_container


router = Router(tags=["Reviews"])


@router.post(
    "products/{product_id}",
    response=ApiResponse[ReviewOutSchema],
    operation_id="createReview",
)
def create_review(
    request: HttpResponse,
    product_id: int,
    schema: ReviewInSchema,
    token: str = Header(alias="Auth-Token"),
) -> ApiResponse[ReviewOutSchema]:
    container = get_container()
    use_case: CreateReviewUseCase = container.resolve(CreateReviewUseCase)

    try:
        review: ReviewEntity = use_case.execute(
            customer_token=token,
            product_id=product_id,
            review=schema.to_entity(),
        )
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message,
        )
    return ApiResponse(
        data=ReviewOutSchema.from_entity(review),
    )
