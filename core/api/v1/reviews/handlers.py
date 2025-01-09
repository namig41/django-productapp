from datetime import datetime

from django.http import HttpResponse
from ninja import (
    Header,
    Router,
)
from ninja.errors import HttpError

from apps.common.exception import ServiceException
from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import (
    CreateReviewOutSchema,
    CreateReviewSchema,
    ReviewInSchema,
)
from project.containers import get_container


router = Router(tags=["Reviews"])


@router.post(
    "products/{product_id}",
    response=ApiResponse[CreateReviewOutSchema],
    operation_id="createReview",
)
def create_review(
    request: HttpResponse,
    product_id: int,
    schema: ReviewInSchema,
    token: str = Header(alias="Auth-Token"),
) -> ApiResponse[CreateReviewOutSchema]:
    create_schema = CreateReviewSchema(
        product_id=product_id,
        customer_token=token,
        review=schema,
    )

    get_container()
    try:
        create_schema.construct()
    except ServiceException as exception:
        raise HttpError(status_code=400, message=exception.message)

    return ApiResponse(
        data=CreateReviewOutSchema(
            rating=1,
            text="Text",
            id=1,
            created_at=datetime.now(),
            updated_at=None,
        ),
    )
