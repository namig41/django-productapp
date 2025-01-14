from dataclasses import dataclass

from core.app.customers.entities import Customer
from core.app.customers.services.customers import BaseCustomerService
from core.app.products.entities.products import Product as ProductEntity
from core.app.products.entities.reviews import Review as ReviewEntity
from core.app.products.services.products import BaseProductService
from core.app.products.services.reviews import (
    BaseReviewService,
    BaseReviewValidatorService,
)


@dataclass
class CreateReviewUseCase:
    review_service: BaseReviewService
    customer_service: BaseCustomerService
    product_service: BaseProductService
    validator_service: BaseReviewValidatorService

    def execute(
        self,
        customer_token: str,
        product_id: int,
        review: ReviewEntity,
    ) -> ReviewEntity:
        customer: Customer = self.customer_service.get_by_token(token=customer_token)
        product: ProductEntity = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validate(
            review=review,
            customer=customer,
            product=product,
        )
        saved_review: ReviewEntity = self.review_service.save_review(
            product=product,
            customer=customer,
            review=review,
        )

        return saved_review
